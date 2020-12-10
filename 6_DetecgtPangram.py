import string


def is_pangram(s):
    return set(list('abcdefghijklmnopqrstuvwxyz')).issubset(set(list(s.lower())))


# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())


# def is_pangram(s):
#     s = s.lower()
#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         if char not in s:
#             return False
#     return True


# def is_pangram(s):
#     s = s.lower()
#     return all(letter in s for letter in string.lowercase)


if __name__ == '__main__':
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
