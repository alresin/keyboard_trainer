def log(*args):
    # print(*args)
    pass


def match(key, target, mod):
    log('key:', key, 'target:', target, 'res:', key == target)
    if (key == target): return True
    if (key not in e2E): return False
    if ('shift' in mod) ^ ('capslock' in mod):
        # capitalized
        return (e2R[key] == target) or (e2E[key] == target)
    else:
        # lower
        return (key == target) or (e2r[key] == target)
