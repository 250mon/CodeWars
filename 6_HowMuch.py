def howmuch(m, n):
    (high, low) = (m, n) if m > n else (n, m) # instead, use min() max()
    lst = []
    for f in range(low, high + 1):
        if f % 7 == 2 and f % 9 == 1:
            b, c = f // 7, f // 9
            lst.append([f"M: {f}", f"B: {b}", f"C: {c}"])
    return lst


if __name__ == '__main__':
    result = howmuch(1, 100)
    print(result)
