from config import DEBUG, APP_NAME, WINDOW_SIZE, MAX_SPEED, HINT_TEXT

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.app import App

from utils import log


Window.size = WINDOW_SIZE
Window.title = APP_NAME


class KeyboardTrainApp(App):
    def __init__(self, kt):
        super().__init__()
        self.kt = kt

    def build(self):
        self.MainLayout = FloatLayout()
        self.MenuBackgroundWidget = MenuBackground()
        self.MainLayout.add_widget(self.MenuBackgroundWidget)

        Menu = BoxLayout(spacing=3,
                         orientation='vertical',
                         size_hint=(.5, .3),
                         pos_hint={'top': 0.5, 'right': 0.75})
        self.MainLayout.add_widget(Menu)

        self.TextInputWidget = TextInput(hint_text=HINT_TEXT,
                                         multiline=False)
        Menu.add_widget(self.TextInputWidget)
        Menu.add_widget(Button(text='Start',
                               on_press=self.kt.newInput))
        Menu.add_widget(Button(text='Exit',
                               on_press=self.kt.exit))
        LabelWidget = Label(text="Keyboard train",
                            pos_hint={'top': 1.2},
                            font_size=60,
                            color=(.2, .2, .2, 1))
        self.MainLayout.add_widget(LabelWidget)

        return self.MainLayout

    def newPhrase(self, KeyboardInput, text):
        self.MainLayout.clear_widgets()
        self.MainLayout.add_widget(self.MenuBackgroundWidget)

        self.TextLabel = Label(text=text,
                               markup=True,
                               color=(.0, .0, .0, 1),
                               font_size=30)
        self.MainLayout.add_widget(self.TextLabel)

        self.MainLayout.add_widget(KeyboardInput.listener)

    def addLetter(self, index, text):
        self.TextLabel.text = '[color=ff0000]' + text[:index] +\
                                '[/color]' + text[index:]

    def endMenu(self, speed, mistakes):
        self.MainLayout.clear_widgets()
        self.MainLayout.add_widget(self.MenuBackgroundWidget)

        Menu = BoxLayout(spacing=3,
                         orientation='vertical',
                         size_hint=(.5, .3),
                         pos_hint={'top': 0.5, 'right': 0.75})
        self.MainLayout.add_widget(Menu)

        self.TextInputWidget = TextInput(hint_text=HINT_TEXT,
                                         multiline=False)
        Menu.add_widget(self.TextInputWidget)
        Menu.add_widget(Button(text='Start',
                               on_press=self.kt.newInput))
        Menu.add_widget(Button(text='Exit',
                               on_press=self.kt.exit))

        if speed < MAX_SPEED:
            formedSpeed = str(round(speed, 1))
        else:
            formedSpeed = ('>' + str(MAX_SPEED))
        newText = "Speed: " + formedSpeed + '\nmistakes: ' + str(mistakes)
        LabelWidget = Label(text=newText,
                            pos_hint={'top': 1.2},
                            font_size=40,
                            color=(.2, .2, .2, 1))
        self.MainLayout.add_widget(LabelWidget)


class MenuBackground(Widget):
    def __init__(self):
        super().__init__()

        with self.canvas:
            Color(.89, .89, .71, 1)
            Rectangle(pos=(0, 0),
                      size=WINDOW_SIZE)


class KeyboardListener(Widget):
    def __init__(self, triggerFunc):
        super().__init__()
        self.trigger_func = triggerFunc

        self._keyboard = Window.request_keyboard(
                        self._keyboard_closed, self, 'text')

        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        log('shutting down keyboard')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        needToRelease = self.trigger_func(keycode, text, modifiers)
        if needToRelease:
            keyboard.release()

        return True
