def is_interesting(number, awesome_phrases):
    if number < 98:
        return 0

    retval = 2
    for index, num_str in enumerate([str(n) for n in range(number, number + 3)]):
        if index > 0:
            retval = 1

        if (length := len(num_str)) < 3:
            continue

        if num_str.count('0') == length - 1:
            return retval
        elif num_str.count(num_str[0]) == length:
            return retval
        elif num_str in [str(phrase) for phrase in awesome_phrases]:
            return retval
        elif False not in [num_str[i] == num_str[length - 1 - i] for i in range(length // 2)]:
            return retval
        elif False not in [(int(num_str[i]) + 1) % 10 == int(num_str[i + 1]) % 10 for i in range(length - 1)]:
            return retval
        elif False not in [int(num_str[i]) - 1 == int(num_str[i + 1]) for i in range(length - 1)]:
            return retval

    return 0

"""[::-1], set, zip, any"""
# def is_incrementing(number): return str(number) in '1234567890'
# def is_decrementing(number): return str(number) in '9876543210'
# def is_palindrome(number):   return str(number) == str(number)[::-1]
# def is_round(number):        return set(str(number)[1:]) == set('0')
# def is_interesting(number, awesome_phrases):
#     tests = (is_round, is_incrementing, is_decrementing, is_palindrome, awesome_phrases.__contains__)
#     for num, color in zip(range(number, number + 3), (2, 1, 1)):
#         if num >= 100 and any(test(num) for test in tests):
#             return color
#     return 0


"""zip"""
# def is_interesting(number, awesome_phrases):
#     for r, num in zip((2, 1, 1), range(number, number + 3)):
#         num_str = str(num)
#         if num in awesome_phrases or num > 99 and (int(num_str[1:]) == 0 or num_str[::-1] == num_str or num_str in '1234567890' or num_str in '9876543210'):
#             return r
#     return 0


"""all, [::-1], zip"""
# def is_interesting(number, awesome_phrases):
#     def check(n):
#         nonlocal awesome_phrases
#         n = str(n)
#         test0 = lambda x: len(x) > 2
#         test1 = lambda x: set(x[1:]) == set("0")
#         test2 = lambda x: len(set(x)) == 1
#         test3 = lambda x: all((int(b) or 10) - (int(a) or 10) == 1 for a, b in zip(x, x[1:]))
#         test4 = lambda x: all(int(a) - int(b) == 1 for a, b in zip(x, x[1:]))
#         test5 = lambda x: x == x[::-1]
#         test6 = lambda x: int(x) in awesome_phrases
#         return test0(n) and (test1(n) or test2(n) or test3(n) or test4(n) or test5(n) or test6(n))
#     return int((check(number) and 2) or (check(number+1) or check(number+2)))


if __name__ == '__main__':
    print(is_interesting(98, [1337]))
