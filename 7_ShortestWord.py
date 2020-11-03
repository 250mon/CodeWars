def find_short(s):
    lst = [len(subs) for subs in s.split()]
    l = min(lst)
    return l


# def find_short(s):
#     return min(len(x) for x in s.split())


# def find_short(s):
#     return len(min(s.split(' '), key=len))


# def find_short(s):
#     return min(map(len, s.split(' ')))


if __name__ == '__main__':
    print(find_short("bitcoin take over the world maybe who knows perhaps"))
