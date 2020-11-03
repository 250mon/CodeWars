from itertools import accumulate


def sum_of_n(n):
    sign = 1 if n >= 0  else -1
    return [(i + 1) * i * sign / 2 for i in range(n * sign + 1)]


"""sum, xrange"""
# def sum_of_n(n):
#     return [(-1 if n < 0 else 1) * sum(xrange(i+1)) for i in xrange(abs(n)+1)]


"""cmp"""
# def sum_of_n(n):
#     return [cmp(n, 0) * sum(range(i + 1)) for i in range(abs(n) + 1)]


"""tuple and condition"""
# def sum_of_n(n):
#     sign, n = (1, -1)[n < 0], abs(n)
#     return [sign * (i * i + i) / 2 for i in range (n + 1)]


"""itertools.accumulate"""
# def sum_of_n(n):
#     if n >= 0:
#         return list(accumulate(range(n+1)))
#     return list(accumulate(range(0, n-1, -1)))


if __name__ == '__main__':
    print(sum_of_n(5))
