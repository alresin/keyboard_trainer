from utils import log, match, calculateSpeed, readFromJson, sendToJson
from gui import KeyboardTrainApp, KeyboardListener
from processing import blendAndShow

from collections import defaultdict
import time


class KeyboardTrainer:
    """Main class of the logical part of the keyboard trainer"""
    def __init__(self):
        """Build the app and run it"""
        self.app = KeyboardTrainApp(self)
        self.app.run()

    def newInput(self, instance):
        """Starts new phase of input with text from the textarea"""
        log('new')
        insertedText = self.app.TextInputWidget.text
        log('inserted text:', insertedText)

        if (len(insertedText) == 0):
            return

        keyboardInput = KeyboardInput(insertedText, self.app, self.endInput)
        self.app.newPhrase(keyboardInput, insertedText)

    def endInput(self, textLen, totalClicks, inputTime, wrongLetters):
        """Move current data to the file with statistics
        and show the menu with statistics"""
        nowSpeed = calculateSpeed(textLen, inputTime)
        nowMistakes = totalClicks - textLen

        data = readFromJson()
        if 'averageSpeed' in data:
            data['averageSpeed'] *= data['totalClicks']
            data['averageSpeed'] += totalClicks * nowSpeed
            data['totalClicks'] += totalClicks
            data['averageSpeed'] /= data['totalClicks']
            newWrongLetters = defaultdict(int)
            for letter in data['wrongLetters']:
                newWrongLetters[letter] = data['wrongLetters'][letter]
            for letter in wrongLetters:
                newWrongLetters[letter] += wrongLetters[letter]
            data['wrongLetters'] = newWrongLetters
        else:
            data['averageSpeed'] = nowSpeed
            data['totalClicks'] = totalClicks
            data['wrongLetters'] = wrongLetters
        sendToJson(data)

        log('You wrote it!')
        log('Your speed:', nowSpeed)
        log('Your time:', round(inputTime, 1))
        log('Your mistakes:', nowMistakes)
        log('Your average speed:', data['averageSpeed'])

        self.app.endMenu(nowSpeed, nowMistakes, data['averageSpeed'])

    def reset(self, instance):
        """Delete all saved statistics"""
        sendToJson({})
        self.endInput(0, 0, 10, {})

    def mostMissButtons(self):
        """Return the a list with buttons
        with most mistakes from statistic file"""
        data = readFromJson()
        if 'wrongLetters' in data:
            heatmap = [(-c, l) for (l, c) in data['wrongLetters'].items()]
            heatmap.sort()
            return ' '.join([str(x[1]) for x in heatmap][:5])
        else:
            return 'No statistics yet'

    def showHeatmap(self, instance):
        """Make a heatmap of mistakes buttons and show it"""
        data = readFromJson()
        blendAndShow(data['wrongLetters'])

    def exit(self, instance):
        """Exit the app"""
        log('Exit')
        exit()


class KeyboardInput:
    """Class of the one input phase. Getting input and return it to the app"""
    letterNumber = 0
    startTime = 0
    totalClicks = 0
    wrongLetters = defaultdict(int)

    def __init__(self, text, app, endFunc):
        """Setting up the object and bind the keyboard listener"""
        self.text = text
        self.app = app
        self.endFunc = endFunc
        self.listener = KeyboardListener(self.onKeyDown)

    def onKeyDown(self, keycode, text, modifiers):
        """Fires in key down event.
        Collect new statistic and starts redrawing window"""
        log('The key', keycode, 'have been pressed')
        log(' - modifiers are %r' % modifiers)

        if (self.startTime == 0):
            self.startTime = time.time()

        if len(keycode[1]) == 1 or keycode[1] == 'spacebar':
            self.totalClicks += 1

        if (match(text, self.text[self.letterNumber], modifiers)):
            log('Right letter!!!')
            self.letterNumber += 1
            self.app.addLetter(self.letterNumber, self.text)
        else:
            log('Wrong letter!!!')
            self.wrongLetters[self.text[self.letterNumber]] += 1

        if len(self.text) == self.letterNumber:
            self.endInput()
            return True

    def endInput(self):
        """Runs trigger function for the end of the input"""
        endTime = time.time()
        self.endFunc(self.letterNumber, self.totalClicks,
                     endTime - self.startTime, self.wrongLetters)
