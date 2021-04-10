from config import e2E, e2r, e2R, DEBUG, STAT_FILE_NAME, MAX_SPEED

import json


def log(*args):
    """Just as print, but only if DEBUG == True"""
    if DEBUG:
        print(*args)


def match(key, target, mod):
    """Answer does the pressed key match with target letter"""
    if (key == target):
        return True
    if (key not in e2E):
        return False
    if ('shift' in mod) ^ ('capslock' in mod):
        # capitalized
        return (e2R[key] == target) or (e2E[key] == target)
    else:
        # lower
        return (key == target) or (e2r[key] == target)


def calculateSpeed(lettersNumber, time):
    """Calculate speed from number of input letters and imput time"""
    return 60 * lettersNumber / time


def readFromJson():
    """Read statistics from file and return it as dictionary"""
    file = open(STAT_FILE_NAME, 'r')
    data = json.load(file)
    file.close()
    return data


def sendToJson(data):
    """Take dictionary with new statistics and write it to the file"""
    file = open(STAT_FILE_NAME, 'w')
    json.dump(data, file)
    file.close()


def formSpeed(speed):
    """Limits the speed for the beautiful output"""
    if speed < MAX_SPEED:
        return str(round(speed, 1))
    else:
        return '>' + str(MAX_SPEED)
