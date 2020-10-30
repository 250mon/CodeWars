lst = []


def start(fn):
    if fn == end:
        return end()
    else:
        return fn


def push(x):
    lst.append(x)
    return start


def add(fn):
    lst.append(lst.pop() + lst.pop())
    return start(fn)


def sub(fn):
    lst.append(lst.pop() - lst.pop())
    return start(fn)


def mul(fn):
    lst.append(lst.pop() * lst.pop())
    return start(fn)


def div(fn):
    lst.append(lst.pop() // lst.pop())
    return start(fn)


def end():
    return lst.pop()


if __name__ == '__main__':
    print((start)(push)(2)(push)(5)(div)(push)(3)(push)(8)(mul)(mul)(end))

