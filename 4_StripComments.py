# def solution(string, markers):
#     src_splits = string.splitlines()
#     result = []
#     for src in src_splits:
#         marker_pos = len(src)
#         for cmt in markers:
#             if cmt in src: marker_pos = min(marker_pos, src.find(cmt))
#         result.append(src[:marker_pos].rstrip())
#     return "\n".join(result)


"""split"""
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


"""re.escape, re.split"""
# from re import split, escape
#
#
# def solution(string, markers):
#     if markers:
#         pattern = "[" + escape("".join(markers)) + "]"
#     else:
#         pattern = ''
#     return '\n'.join(split(pattern, line)[0].rstrip() for line in string.splitlines())




if __name__ == '__main__':
    result = solution("apples, !pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    # result should == "apples, pears\ngrapes\nbananas"
    print(result)
