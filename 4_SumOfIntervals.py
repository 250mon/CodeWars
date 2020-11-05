"""different ways to create a set, union"""
def sum_of_intervals(intervals):
    total_set = set()
    for elem in intervals:
        #each_set = {x for x in range(*elem)}
        #each_set = set([*range(*elem)])
        each_set = {*range(*elem)}
        total_set = total_set.union(each_set)
    return len(total_set)

"""revised my sol; set.add() accepts only a single element"""
# def sum_of_intervals(intervals):
#     total_set = set()
#     for elem in intervals:
#         for x in range(*elem):
#             total_set.add(x)
#     return len(total_set)


"""multiple assignment, sorted"""
# def sum_of_intervals(intervals):
#     sum, top = 0, float("-inf")
#     for a,b in sorted(intervals):
#         if top < a: top = a
#         if top < b: sum, top = sum+b-top, b
#     return sum


"""for inside for"""
# def sum_of_intervals(intervals):
#     t_set = set([n for (a, b) in intervals for n in [i for i in range(a, b)]])
#     return len(t_set)


if __name__ == '__main__':
    print(sum_of_intervals([
        (1, 4),
        (7, 10),
        (3, 5)
    ]))
