from config import DEBUG, APP_NAME, WINDOW_SIZE, HINT_TEXT, BACKGROUND_COLOR
from utils import log, formSpeed

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.app import App


Window.size = WINDOW_SIZE
Window.title = APP_NAME
Window.clearcolor = BACKGROUND_COLOR


class KeyboardTrainApp(App):
    """Main class of gui part of the keyboard trainer"""
    def __init__(self, kt):
        """Initialization of the app.
        Just set the reference to the main logic class of the app.
        """
        super().__init__()
        self.kt = kt

    def build(self):
        """Start function of the app.
        Draw the start menu.
        """
        self.MainLayout = FloatLayout()

        self.makeMenu()

        LabelWidget = Label(text="Keyboard train",
                            pos_hint={'top': 1.3},
                            font_size=50,
                            color=(.2, .2, .2, 1))
        self.MainLayout.add_widget(LabelWidget)

        return self.MainLayout

    def newPhrase(self, KeyboardInput, text):
        """Begins a new phase of the letter input"""
        self.MainLayout.clear_widgets()

        self.TextLabel = Label(text=text,
                               markup=True,
                               color=(.0, .0, .0, 1),
                               font_size=30)
        self.MainLayout.add_widget(self.TextLabel)

        self.MainLayout.add_widget(KeyboardInput.listener)

    def addLetter(self, index, text):
        """Change the letter color during the input phase"""
        print(Window.size)
        self.TextLabel.text = '[color=ff0000]' + text[:index] +\
                              '[/color]' + text[index:]

    def endMenu(self, speed, mistakes, averageSpeed):
        """Draw the menu of with statistics and buttons start and exit"""
        self.MainLayout.clear_widgets()

        self.makeMenu()

        newText = "Speed: " + formSpeed(speed) + '\nMistakes: ' + str(mistakes)
        newText += '\nAverage speed: ' + formSpeed(averageSpeed)
        newText += '\nMost mistakes buttons: ' + self.kt.mostMissButtons()
        LabelWidget = Label(text=newText,
                            pos_hint={'top': 1.3},
                            font_size=30,
                            color=(.2, .2, .2, 1))
        self.MainLayout.add_widget(LabelWidget)

    def makeMenu(self):
        """Make menu with buttons and textarea"""
        Menu = BoxLayout(spacing=3,
                         orientation='vertical',
                         size_hint=(.5, .5),
                         pos_hint={'top': 0.6, 'right': 0.75})
        self.MainLayout.add_widget(Menu)

        self.TextInputWidget = TextInput(hint_text=HINT_TEXT,
                                         multiline=False)
        Menu.add_widget(self.TextInputWidget)
        Menu.add_widget(Button(text='Start',
                               on_press=self.kt.newInput))
        Menu.add_widget(Button(text='Show mistakes heatmap',
                               on_press=self.kt.showHeatmap))
        Menu.add_widget(Button(text='Reset statistics',
                               on_press=self.kt.reset))
        Menu.add_widget(Button(text='Exit',
                               on_press=self.kt.exit))


class KeyboardListener(Widget):
    """Make and set a listener object to the keyboard"""
    def __init__(self, triggerFunc):
        """Make keyboard and bind it to the window"""
        super().__init__()
        self.triggerFunc = triggerFunc

        self._keyboard = Window.request_keyboard(
                        self._keyboard_closed, self, 'text')

        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        """Unbind keyboard from the window"""
        log('shutting down keyboard')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        """Activate trigger function and release keyboard if needed"""
        needToRelease = self.triggerFunc(keycode, text, modifiers)
        if needToRelease:
            keyboard.release()

        return True
