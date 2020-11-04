import re


def remove_parentheses(s):
    while (t := re.sub(r'\([^()]*\)', '', s)) != s:
        s = t
    return s


# def remove_parentheses(s):
#     lvl, result = 0, []
#     for c in s:
#         if lvl > 0 or c == '(':
#             if c == '(':
#                 lvl += 1
#             if c == ')':
#                 lvl -= 1
#             else:
#                 pass
#         else:
#             result.append(c)
#     return "".join(result)


# def remove_parentheses(s):
#     lvl, out = 0, []
#     for c in s:
#         lvl += (c == '(')
#         if not lvl:
#             out.append(c)
#         lvl -= (c == ')')
#     return ''.join(out)


if __name__ == '__main__':
    s = "my name is (so(ng)) jye young"
    result1 = remove_parentheses(s)
    print(result1)
