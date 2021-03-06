import random


class Befunge:

    def __init__(self, code):
        self.code = code
        self.code_characters = []
        self.stack = []
        self.x = 0
        self.y = 0
        self.x_max = 0
        self.y_max = 0
        self.x_right = True
        self.y_down = True
        self.move_hor = True
        self.ascii_mode = False
        self.skip = False
        self.run = True
        self.output = []
        self.binary_op = {
            '+': lambda a, b: int.__add__(a, b),
            '-': lambda a, b: int.__sub__(b, a),
            '*': lambda a, b: int.__mul__(a, b),
            '/': lambda a, b: int.__floordiv__(b, a) if a != 0 else 0,
            '%': lambda a, b: int.__mod__(b, a) if a != 0 else 0,
            '`': lambda a, b: int(b > a),
        }

    def extract_code_characters(self):
        lines = self.code.splitlines()
        self.x_max = max(map(len, lines))
        self.y_max = len(lines)
        self.code_characters = list(map(list, lines))

    def operation(self, op):
        a, b = self.stack.pop(), self.stack.pop()
        self.stack.append(op(a, b))

    def set_direction(self, direction):
        if direction == '>':
            self.move_hor = True
            self.x_right = True
        elif direction == '<':
            self.move_hor = True
            self.x_right = False
        elif direction == 'v':
            self.move_hor = False
            self.y_down = True
        else:
            self.move_hor = False
            self.y_down = False

    def move_to_next(self):
        # Move the pointer
        if self.move_hor:
            if self.x_right:
                self.x = self.x + 1
                if self.x == self.x_max:
                    self.x = 0
                    self.y = self.y + 1 if self.y < self.y_max else 0
            else:
                self.x = self.x - 1
                if self.x == -1:
                    self.x = self.x_max - 1
                    self.y = self.y - 1 if self.y > 0 else self.y_max - 1
        else:
            if self.y_down:
                self.y = self.y + 1
                if self.y == self.y_max:
                    self.y = 0
                    self.x = self.x + 1 if self.x < self.x_max else 0
            else:
                self.y = self.y - 1
                if self.y == -1:
                    self.y = self.y_max - 1
                    self.x = self.x - 1 if self.x > 0 else self.x_max - 1

    def interpret_instructions(self, inst):
        if self.skip:
            self.skip = False
        elif self.ascii_mode and inst != '"':
            self.stack.append(int.from_bytes(bytes(inst, encoding='utf-8'), byteorder='big'))
        elif inst.isdigit():
            self.stack.append(int(inst))
        elif inst in '+-*/%`':
            a, b = self.stack.pop(), self.stack.pop()
            self.stack.append(self.binary_op[inst](a, b))
        elif inst == '!':
            if self.stack.pop(): self.stack.append(0)
            else: self.stack.append(1)
        elif inst in '><v^':
            self.set_direction(inst)
        elif inst == '?':
            self.set_direction(random.choice(['>', '<', 'v', '^']))
        elif inst == '_':
            a = self.stack.pop()
            if a == 0:
                self.set_direction('>')
            else:
                self.set_direction('<')
        elif inst == '|':
            a = self.stack.pop()
            if a == 0:
                self.set_direction('v')
            else:
                self.set_direction('^')
        elif inst == '"':
            if self.ascii_mode:
                self.ascii_mode = False
            else:
                self.ascii_mode = True
        elif inst == ':':
            if len(self.stack) == 0:
                x = 0
            else:
                x = self.stack[-1]
            self.stack.append(x)
        elif inst == '\\':
            assert len(self.stack) > 0, 'The stack size should be greater than 0'
            if len(self.stack) == 1:
                self.stack[0] = 0
            else:
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a)
                self.stack.append(b)
        elif inst == '$':
            self.stack.pop()
        elif inst == '.':
            self.output.append(str(self.stack.pop()))
        elif inst == ',':
            # a is supposed to be a ASCII byte
            a = self.stack.pop()
            # if a is an int type, convert it to a ASCII byte
            if isinstance(a, int): a = a.to_bytes(1, byteorder='big')

            # Converting the ASCII code to a character for output
            self.output.append(a.decode(encoding="utf-8"))
        elif inst == '#':
            self.skip = True
        elif inst == 'p':
            y, x, v = self.stack.pop(), self.stack.pop(), self.stack.pop()
            # Converting the ASCII code to a character
            self.code_characters[y][x] = v.to_bytes(1, byteorder='big').decode(encoding="utf-8")
        elif inst == 'g':
            y, x = self.stack.pop(), self.stack.pop()
            # Converting the character to an ASCII code
            self.stack.append(int.from_bytes(bytes(self.code_characters[y][x], encoding="utf-8"), byteorder='big'))
        elif inst == '@':
            self.run = False
        else:
            pass

    def walk_through(self):
        self.extract_code_characters()
        while self.run:
            if self.x < len(self.code_characters[self.y]):
                code_ch = self.code_characters[self.y][self.x]
                self.interpret_instructions(code_ch)
            self.move_to_next()


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
        ' 12345',
        ' ^?^',
        '> ? ?^',
        ' v?v',
        ' 6789',
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
    bf = Befunge(code := '\n'.join(code5_arr))
    bf.walk_through()
    print(''.join(bf.output))
