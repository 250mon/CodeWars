def flatten_list(n_list):
    result_list = []
    if not n_list:
        return result_list
    stack = [list(n_list)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num:
            stack.append(c_num)
        if isinstance(next, list):
            if next:
                stack.append(list(next))
        else:
            result_list.append(next)
    result_list.reverse()
    return result_list


if __name__ == '__main__':
    test_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, [100, 110], 120]]
    result = flatten_list(test_list)
    print(result)