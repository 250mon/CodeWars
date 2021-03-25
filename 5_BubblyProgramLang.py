"""My solution: made each token a particular function"""
# lst = []
# def start(fn):
#     if fn == end:
#         return end()
#     else:
#         return fn
#
# def push(x):
#     lst.append(x)
#     return start
#
# def add(fn):
#     lst.append(lst.pop() + lst.pop())
#     return start(fn)
#
# def sub(fn):
#     lst.append(lst.pop() - lst.pop())
#     return start(fn)
#
# def mul(fn):
#     lst.append(lst.pop() * lst.pop())
#     return start(fn)
#
# def div(fn):
#     lst.append(lst.pop() // lst.pop())
#     return start(fn)
#
# def end():
#     return lst.pop()


"""Callable class / Multiple assignments"""
"""made a callable class 'start' and each token just an argument"""
end, push, add, sub, mul, div = 'end push add sub mul div'.split()
OPS = {add: int.__add__, sub: int.__sub__, mul: int.__mul__, div: int.__floordiv__}


class start:
    def __init__(self, f):
        self.stk = []

    def __call__(self, x):
        if x == end: return self.stk[-1]
        op = OPS.get(x)
        if op:
            a, b = self.stk.pop(), self.stk.pop()
            self.stk.append(op(a, b))
        elif isinstance(x, int):
            self.stk.append(x)
        return self


if __name__ == '__main__':
    print((start)(push)(2)(push)(5)(div)(push)(3)(push)(8)(mul)(mul)(end))

