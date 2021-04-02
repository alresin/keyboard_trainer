from utils import log, match, calculateSpeed
from gui import KeyboardTrainApp, KeyboardListener
from time import time


class KeyboardTrainer:
    def __init__(self):
        self.app = KeyboardTrainApp(self)
        self.app.run()

    def newInput(self, instance):
        log('new')
        insertedText = self.app.TextInputWidget.text
        log('inserted text: ', insertedText)

        if (len(insertedText) == 0):
            return

        keyboardInput = KeyboardInput(insertedText, self.app, self.app.endMenu)
        self.app.newPhrase(keyboardInput, insertedText)

    def exit(self, instance):
        log('Exit')
        exit()


class KeyboardInput:
    letterNumber = 0
    startTime = 0
    totalClicks = 0

    def __init__(self, text, app, endFunc):
        self.text = text
        self.app = app
        self.endFunc = endFunc
        self.listener = KeyboardListener(self.onKeyDown)

    def onKeyDown(self, keycode, text, modifiers):
        log('The key', keycode, 'have been pressed')
        log(' - modifiers are %r' % modifiers)

        if (self.startTime == 0):
            self.startTime = time()

        if len(keycode[1]) == 1 or keycode[1] == 'spacebar':
            self.totalClicks += 1

        if (match(text, self.text[self.letterNumber], modifiers)):
            log('Right letter!!!')
            self.letterNumber += 1
            self.app.addLetter(self.letterNumber, self.text)

        if len(self.text) == self.letterNumber:
            self.endInput()
            return True

    def endInput(self):
        endTime = time()
        speed = calculateSpeed(self.letterNumber, self.startTime,  endTime)
        mistakes = self.totalClicks - self.letterNumber
        print('You wrote it!')
        print('Your speed:', speed)
        print('Your time:', round(endTime - self.startTime, 1))
        print('Your mistakes:', mistakes)
        self.endFunc(speed, mistakes)
