def automorphic(n):
    x = len(str(n))
    return 'Automorphic' if (n ** 2) % (10 ** x) == n else 'Not!!'

"""some_str.endswith(other_str)"""
# def automorphic(n):
#     return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!"

if __name__ == '__main__':
    print(automorphic(76)) # automorphic
    print(automorphic(95)) # Not!!