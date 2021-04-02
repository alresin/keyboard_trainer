from config import DEBUG
from config import e2E, e2r, e2R


def log(*args):
    if DEBUG:
        print(*args)


def match(key, target, mod):
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


def calculateSpeed(lettersNumber, sTime, eTime):
    return 60 * lettersNumber / (eTime - sTime)
