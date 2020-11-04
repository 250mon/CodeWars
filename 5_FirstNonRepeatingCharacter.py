# def first_non_repeating_letter(string):
#     for c in string:
#         if string.lower().count(c.lower()) == 1:
#             return c
#     return ''


"""generator expression, built-in function 'next(iterator[,default])"""
def first_non_repeating_letter(string):
    return next((x for x in string if string.lower().count(x.lower())==1), '')


"""list comprehensions"""
# def first_non_repeating_letter(string):
#     singles = [i for i in string if string.lower().count(i.lower()) == 1]
#     return singles[0] if singles else ''


if __name__ == '__main__':
    print(first_non_repeating_letter('sTreSS'))