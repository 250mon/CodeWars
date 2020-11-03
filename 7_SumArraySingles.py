from collections import Counter


def repeats(arr):
    return sum(k for k, v in Counter(arr).items() if v == 1)


# def repeats2(arr):
#     return sum([x for x in arr if arr.count(x) == 1])


"""set()"""
# repeats3 = lambda a: 2 * sum(set(a)) - sum(a)


if __name__ == '__main__':
    result = repeats([4, 5, 7, 5, 4, 8])
    print(result)