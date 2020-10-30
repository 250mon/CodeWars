import math


def solve(p):
    num = p * 123456789
    org_num = str(num)
    str_num = '0' * (3 - len(org_num) % 3) + org_num
    lst = [int(str_num[i * 3: (i + 1) * 3]) for i in range(math.ceil(len(str_num) / 3))]
    return sum(lst)


if __name__ == '__main__':
    print(solve(37))
