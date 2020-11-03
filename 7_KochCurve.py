def koch_curve(n):
    lst = []
    powers_of_four = [4 ** i for i in range(n)]
    powers_of_four.reverse()
    for index in range(1, 4 ** n):
        coeff = []
        for i in powers_of_four:
            coeff.append(index // i)
            index %= i
        while (final := coeff.pop()) == 0:
            pass
        lst.append(-120 if final == 2 else 60)
    return lst


"""recursive, unpacking a list"""
# def koch_curve(n):
#     if not n: return []
#     deep = koch_curve(n-1)
#     return [*deep, 60, *deep, -120, *deep, 60, *deep]


"""combining the lists"""
# def koch_curve(n):
#     l = []
#     for i in range(1, n + 1):
#         l = l + [60] + l + [-120] + l + [60] + l
#     return l


if __name__ == '__main__':
    print(koch_curve(3))
