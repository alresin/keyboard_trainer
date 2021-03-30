from config import *
from utils import *

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


class KeyboardTrainApp(App):
    def build(self):
        self.MainLayout = FloatLayout()
        MenuBackgroundWidget = MenuBackground()
        self.MainLayout.add_widget(MenuBackgroundWidget)
        
        Menu = BoxLayout(spacing = 3,
                            orientation = 'vertical',
                            size_hint = (.5, .3), 
                            pos_hint = {'top': 0.5, 'right' : 0.75})
        self.MainLayout.add_widget(Menu)

        self.TextInputWidget = TextInput(hint_text='Это предложение для набора текста',
                                        multiline=False)
        Menu.add_widget(self.TextInputWidget)
        Menu.add_widget(Button(text = 'Start',
                                on_press = self.new))
        Menu.add_widget(Button(text = 'Exit',
                                on_press = self.exit))
        LabelWidget = Label(text = "Keyboard train",
                                pos_hint = {'top': 1.2},
                                font_size = 60,
                                color = (.2, .2, .2, 1))
        self.MainLayout.add_widget(LabelWidget)

        return self.MainLayout


    def new(self, instance):
        log('new')
        self.MainLayout.clear_widgets()
        MenuBackgroundWidget = MenuBackground()
        self.MainLayout.add_widget(MenuBackgroundWidget)

        insertedText = self.TextInputWidget.text
        log('inserted text: ', insertedText)
        TextLabel = Label(text = insertedText,
                            markup=True,
                            color = (.0, .0, .0, 1),
                            font_size = 30)
        self.MainLayout.add_widget(TextLabel)

        self.MainLayout.add_widget(keyboardListener(insertedText, TextLabel))


    def exit(self, instance):
        log('Exit')
        exit()


class MenuBackground(Widget):
    def __init__(self):
        super().__init__()

        with self.canvas:
            Color(.89, .89, .71, 1)
            Rectangle(pos = (0, 0), 
                    size = WINDOW_SIZE)


class keyboardListener(Widget):
    letterNumber = 0
    def __init__(self, text, TextLabel):
        super().__init__()
        
        self.text = text
        self.TextLabel = TextLabel
        
        self._keyboard = Window.request_keyboard(
                        self._keyboard_closed, self, 'text')

        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        if len(text) == self.letterNumber:
            self._keyboard_closed()


    def _keyboard_closed(self):
        log('keyboard closed')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
        log('You wrote it!')
        exit()


    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        log('The key', keycode, 'have been pressed')
        log(' - text is %r' % text)
        log(' - modifiers are %r' % modifiers)

        if (match(text, self.text[self.letterNumber], modifiers)):
                log('Right letter!!!')

                self.letterNumber += 1
                self.TextLabel.text = '[color=ff0000]' + self.text[:self.letterNumber] + \
                                        '[/color]' + self.text[self.letterNumber:]

        if len(self.text) == self.letterNumber:
            keyboard.release()

        return True
