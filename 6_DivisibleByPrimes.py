def check(p, base):
    multiple = (base ** (p - 1)) - 1
    for i in range(1, p):
        print(f'{i} is being checked...')
        num, sum, altsum, sign = multiple, 0, 0, 1
        while num:
            divisor = 10 ** i
            remainder = num % divisor
            num = num // divisor
            sum += remainder
            altsum += (remainder * sign)
            sign *= -1
        if sum != altsum and sum % p == 0 or altsum % p == 0:
            return i
        else:
            return False

def solve(p):
    for base in range(2, 10):
        if result := check(p, base):
            return result

if __name__ == '__main__':
    print(solve(7))
