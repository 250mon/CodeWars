from random import choice


def interpret(code):
    code = [list(l) for l in code.split('\n')]
    x, y = 0, 0
    dx, dy = 1, 0
    output = ''
    stack = []
    string_mode = False

    while True:
        move = 1
        i = code[y][x]

        if string_mode:
            if i == '"':
                string_mode = False
            else:
                stack.append(ord(i))
        else:

            if i.isdigit():
                stack.append(int(i))
            elif i == '+':
                stack[-2:] = [stack[-2] + stack[-1]]
            elif i == '-':
                stack[-2:] = [stack[-2] - stack[-1]]
            elif i == '*':
                stack[-2:] = [stack[-2] * stack[-1]]
            elif i == '/':
                stack[-2:] = [stack[-2] and stack[-2] / stack[-1]]
            elif i == '%':
                stack[-2:] = [stack[-2] and stack[-2] % stack[-1]]
            elif i == '!':
                stack[-1] = not stack[-1]
            elif i == '`':
                stack[-2:] = [stack[-2] > stack[-1]]
            elif i in '><^v?':
                if i == '?':   i = choice('><^v')
                if i == '>':
                    dx, dy = 1, 0
                elif i == '<':
                    dx, dy = -1, 0
                elif i == '^':
                    dx, dy = 0, -1
                elif i == 'v':
                    dx, dy = 0, 1
            elif i == '_':
                dx, dy = (-1 if stack.pop() else 1), 0
            elif i == '|':
                dx, dy = 0, (-1 if stack.pop() else 1)
            elif i == '"':
                string_mode = True
            elif i == ':':
                stack.append(stack[-1] if stack else 0)
            elif i == '\\':
                stack[-2:] = stack[-2:][::-1]
            elif i == '$':
                stack.pop()
            elif i == '.':
                output += str(stack.pop())
            elif i == ',':
                output += chr(stack.pop())
            elif i == '#':
                move += 1
            elif i == 'p':
                ty, tx, tv = stack.pop(), stack.pop(), stack.pop()
                code[ty][tx] = chr(tv)
            elif i == 'g':
                ty, tx = stack.pop(), stack.pop()
                stack.append(ord(code[ty][tx]))
            elif i == '@':
                return output

        for _ in range(move):
            x = (x + dx) % len(code[y])
            y = (y + dy) % len(code)


if __name__ == '__main__':
    code1_arr = [
        '>              v',
        'v  ,,,,,"Hello"<',
        '>48*,          v',
        'v,,,,,,"World!"<',
        '>25*,@',
    ]
    code2_arr = [
        '>987v>.v',
        'v456<  :',
        '>321 ^ _@',
    ]
    code3_arr = [
        'v>>>>>v',
        ' 12345 ',
        ' ^?^   ',
        '> ? ?^ ',
        ' v?v   ',
        ' 6789  ',
        ' >>>> v',
        '^    .<',
    ]
    code4_arr = [
        '"!dlrow olleH">:#,_@'
    ]
    code5_arr = [
        '08>:1-:v v *_$.@',
        '  ^    _$>\\:^',
    ]
    code6_arr = [
        '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'
    ]
    code7_arr = [
        '2>:3g" "-!v\  g30          <',
        ' |!`"&":+1_:.:03p>03g+:"&"`|',
        ' @               ^  p3\\" ":<',
        '2 2345678901234567890123456789012345678',
    ]
    output = interpret('\n'.join(code3_arr))
    print(output)
