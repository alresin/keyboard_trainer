from config import *

def log(*args):
    if DEBUG:
        print(*args)


def match(key, target, mod):
    if (key == target): return True
    if (key not in e2E): return False
    if ('shift' in mod) ^ ('capslock' in mod):
        # capitalized
        return (e2R[key] == target) or (e2E[key] == target)
    else:
        # lower
        return (key == target) or (e2r[key] == target)