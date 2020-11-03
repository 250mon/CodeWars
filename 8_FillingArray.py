def arr(*n):
    # [ the numbers 0 to N-1 ]
    if len(n) == 0:
        x = 0
    else:
        x = n[0]
    return list(range(0, x))


"""default argument valuei"""
# def arr(n=0):
#     return list(range(n))


"""unpacking range generator"""
# def arr(n=0):
#     return [*range(n)]


if __name__ == '__main__':
    print(arr())
    print(arr(6))
