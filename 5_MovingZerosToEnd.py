def move_zeros(array):
    new = list(map(lambda x: 0 if isinstance(x, float) and x == 0.0 else x, array))
    return sorted(new, key=lambda x: str(x) == '0' if not isinstance(x, str) else False)


#isinstance()
# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i != 0]
#     return l + [0] * (len(arr) - len(l))


#type()
# def move_zeros(array):
#     return sorted(array, key=lambda x: x == 0 and type(x) is not bool)


#False is 0
# def move_zeros(array):
#     return sorted(array, key=lambda x: x == 0 and x is not False)


if __name__ == '__main__':
    lst = [False, 1, 0, 1, 2, 0, 1, 3, "a"]
    result = move_zeros(lst)
    print(result)
