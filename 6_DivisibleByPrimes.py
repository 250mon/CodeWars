def check(p, base):
    multiple = (base ** (p - 1)) - 1
    print(f'multiple:{multiple}')
    for i in range(1, len(str(multiple))):
        print(f'{i} is being checked...')
        num, sum, altsum, sign = multiple, 0, 0, 1
        while num:
            divisor = 10 ** i
            remainder = num % divisor
            num = num // divisor
            sum += remainder
            altsum += (remainder * sign)
            sign *= -1
        print(f'sum:{sum} altsum:{altsum}')
        if sum % p == 0 or altsum % p == 0:
            if sum == altsum:
                return False
            else:
                return i

def solve(p):
    for base in range(2, 10):
        print(f'base {base} is being checked...')
        if result := check(p, base):
            return result
        print('\n')

if __name__ == '__main__':
    print(solve(41))
