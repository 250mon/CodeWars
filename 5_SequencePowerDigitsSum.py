def sum_pow_dig_seq(start, n, k):
    """My Solution"""
    seq_list = [start]
    h, patt_len, last_term = 0, 0, 0

    for count in range(1, k + 1):
        element = sum_pow(start, n)
        try:
            index = seq_list.index(element)
            h = index
            patt_len = count - index
            cyc_patt_arr = list(seq_list[index:])
            last_term = cyc_patt_arr[(k - h) % patt_len]
            break;
        except ValueError:
            seq_list.append(element)
            start = element

    return [h, cyc_patt_arr, patt_len, last_term]


def sum_pow(num, n):
    if num < 10:
        return num ** n
    return ((num % 10) ** n) + sum_pow(num // 10, n)


def sum_pow_dig_seq2(start, n, k):
    """Good Solution"""
    seq = [start]
    num = start
    for i in range(k):
        num = sum(map(lambda x: int(x) ** n, str(num)))
        #num = sum(int(c) ** n for c in str(num))
        if num in seq:
            # We got the loop!
            loop_starts_from = seq.index(num)
            loop_array = seq[loop_starts_from:]
            tail_size = loop_starts_from
            loop_size = len(loop_array)
            last_term = loop_array[(k - tail_size) % loop_size]
            return [tail_size, loop_array, loop_size, last_term]
        seq.append(num)
    else:
        # What if we didn`t get the loop?
        return [len(seq), [], 0, seq[-1]]


if __name__ == '__main__':
    result = sum_pow_dig_seq(420, 3, 10)
    print(result)
