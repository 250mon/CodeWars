from collections import deque


def sort_array(source_array):
    temp_arr = []
    odd_arr = []
    for x in source_array:
        if x % 2 != 0:
            temp_arr.append('a')
            odd_arr.append(x)
        else:
            temp_arr.append(x)
    odd_arr.sort(reverse=True)
    return [x if x != 'a' else odd_arr.pop() for x in temp_arr]


"""deque(), Q.popleft()"""
# def sort_array(array):
#     odd = deque(sorted(x for x in array if x % 2))
#     return [odd.popleft() if x % 2 else x for x in array]


"""sorted(arr, reverse=True)"""
# def sort_array(arr):
#     odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
#     return [x if x % 2 == 0 else odds.pop() for x in arr]


"""iter()"""
# def sort_array(source_array):
#     odds = iter(sorted(v for v in source_array if v % 2))
#     return [next(odds) if i % 2 else i for i in source_array]


"""enumerate()"""
# def sort_array(source_array):
#     result = sorted([l for l in source_array if l % 2 == 1])
#     for index, item in enumerate(source_array):
#         if item % 2 == 0:
#             result.insert(index, item)
#     return result


if __name__ == '__main__':
    lst = [11, 1, 2, 8, 3, 4, 5]
    result = sort_array(lst)
    print(result)
