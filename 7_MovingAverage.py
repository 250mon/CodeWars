from statistics import mean


def moving_average(values, n):
    if n != 0 and n <= len(values):
        return [mean(values[i: i + n]) for i in range(len(values) - n + 1)]
    else:
        return None


# def moving_average(a, n):
#     if 0 < n <= len(a): return [sum(a[i:i + n]) / n for i in range(len(a) - n + 1)]


# def moving_average(values, n):
#     return [mean(values[i:i + n]) for i in range(len(values) - n + 1)] if n and n <= len(values) else None


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(moving_average(lst, 3))
    print(moving_average(lst, 0))
