def iter_flatten(ll):
    return (x for l in ll for x in l)


def flatten(ll):
    return [x for l in ll for x in l]
