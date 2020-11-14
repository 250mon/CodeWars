
class Befunge:

    def __init__(self, code):
        self.code_characters = list(map(list, code.splitlines()))
        self.stack = []
        self.x = 0
        self.y = 0
        self.x_right = True
        self.y_down = True
        self.move_hor = True
        self.run = True

    def interpret_instructions(self, inst):
        if inst.isdigit():
            self.stack.append(inst)
        elif inst == '+':
            self.stack.append(str(int(self.stack.pop())+int(self.stack.pop())))
        elif inst == '-':
            self.stack.append(str(-1*(int(self.stack.pop())-int(self.stack.pop()))))
        elif inst == '*':
            self.stack.append(str(int(self.stack.pop()) * int(self.stack.pop())))
        elif inst == '/':
            self.stack.append(str(int(self.stack.pop()) / int(self.stack.pop())))
        elif inst == '>':
            self.move_hor = True
            self.x_right = True
        elif inst == '<':
            self.move_hor = True
            self.x_right = False
        elif inst == 'v':
            self.move_hor = False
            self.y_down = True
        elif inst == '^':
            self.move_hor = False
            self.y_down = False
        elif inst == '@':
            self.run = False

        # Move the pointer
        if self.move_hor:
            if self.x_right: self.x = min(80, self.x+1)
            else: self.x = max(0, self.x-1)
        else:
            if self.y_down: self.y = min(25, self.y+1)
            else: self.y = max(0, self.y-1)

    def operation(self, op):
        a, b = self.stack.pop(), self.stack.pop()
        self.stack.append(op(a, b))


    def walk_through(self):
        while(self.run):
            code_ch = self.code_characters[self.y][self.x]
            self.interpret_instructions(code_ch)
        self.output()

    def output(self):
        print(self.stack)


if __name__ == '__main__':
    bf = Befunge('v02>3+@\n>45^')
    bf.walk_through()
