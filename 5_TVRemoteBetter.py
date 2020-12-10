H, W     = 6, 8
KEYBOARD = ["abcde123fghij456klmno789pqrst.@0uvwxyz_/\u000e ",
            "ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/\u000e ",
            "^~?!'\"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡\u000e\u000e\u000e_/\u000e "]
MAP      = [{c: (i // W, i % W) for i, c in enumerate(KEYBOARD[x])} for x in range(len(KEYBOARD))]


def manhattan(*pts):
    dxy = [abs(z2-z1) for z1, z2 in zip(*pts)]
    return 1 + sum(min(dz, Z-dz) for dz, Z in zip(dxy, (H, W)))


def tv_remote(words):
    cnt, mod, was = 0, 0, 'a'
    for c in words:
        while c not in KEYBOARD[mod]:
            cnt += manhattan(MAP[mod][was], MAP[mod]['\u000e'])
            was = '\u000e'
            mod = (mod+1) % 3
        cnt += manhattan(MAP[mod][was], MAP[mod][c])
        was  = c
    return cnt


if __name__ == '__main__':
    print(tv_remote("&wMI7b/ .N"))

"""divmod, recursive"""
# M1 = "abcde123fghij456klmno789pqrst.@0uvwxyz_/° "
# M2 = "ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/° "
# M3 = "^~?!\'\"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡°°°_/° "
#
# D1 = {c: divmod(i, 8) for i, c in enumerate(M1)}
# D2 = {c: divmod(i, 8) for i, c in enumerate(M2)}
# D3 = {c: divmod(i, 8) for i, c in enumerate(M3)}
# D = (D1, D2, D3)
#
# dist = lambda i, j, k, l: min(abs(i - k), 6 - abs(i - k)) + min(abs(j - l), 8 - abs(j - l)) + 1
#
#
# def tv_remote(words):
#     def rec(c, d, i, j):
#         if c == len(words): return 0
#         tmp = D[d].get(words[c])
#         if tmp: return dist(i, j, *tmp) + rec(c + 1, d, *tmp)
#         return dist(i, j, 5, 0) + rec(c, (d + 1) % 3, 5, 0)
#
#     return rec(0, 0, 0, 0)


"""namedtuple, cycle"""
# from collections import namedtuple
# from itertools import repeat, cycle
#
# Position = namedtuple('Position', 'y x')
# shift = Position(5, 0)
#
# remote = (
#     (
#         'a', 'b', 'c', 'd', 'e', '1', '2', '3',
#         'f', 'g', 'h', 'i', 'j', '4', '5', '6',
#         'k', 'l', 'm', 'n', 'o', '7', '8', '9',
#         'p', 'q', 'r', 's', 't', '.', '@', '0',
#         'u', 'v', 'w', 'x', 'y', 'z', '_', '/',
#         '', ' '
#     ),
#     (
#         'A', 'B', 'C', 'D', 'E', '1', '2', '3',
#         'F', 'G', 'H', 'I', 'J', '4', '5', '6',
#         'K', 'L', 'M', 'N', 'O', '7', '8', '9',
#         'P', 'Q', 'R', 'S', 'T', '.', '@', '0',
#         'U', 'V', 'W', 'X', 'Y', 'Z', '_', '/',
#         '', ' '
#     ),
#     (
#         '^', '~', '?', '!', "'", '"', '(', ')',
#         '-', ':', ';', '+', '&', '%', '*', '=',
#         '<', '>', '€', '£', '$', '¥', '¤', '\\',
#         '[', ']', '{', '}', ',', '.', '@', '§',
#         '#', '¿', '¡', '', '', '', '_', '/',
#         '', ' '
#     )
# )
#
#
# def tv_remote(word: str):
#     modes = cycle(remote)
#     prev, mode, button_presses = Position(0, 0), next(modes), 0
#
#     for letter in word:
#         try:
#             i = mode.index(letter)
#
#         except ValueError:
#             button_presses += calc_presses(prev, shift)
#             mode = next(modes)
#             prev = shift
#
#             try:
#                 i = mode.index(letter)
#
#             except ValueError:
#                 button_presses += 1
#                 mode = next(modes)
#                 i = mode.index(letter)
#
#         cur = Position(*divmod(i, 8))
#         button_presses += calc_presses(prev, cur)
#         prev = cur
#
#     return button_presses
#
#
# def calc_presses(pos1: Position, pos2: Position):
#     dif_y, dif_x = abs(pos1.y - pos2.y), abs(pos1.x - pos2.x)
#     return min(dif_y, 6 - dif_y) + min(dif_x, 8 - dif_x) + 1


"""multiple for in generator"""
# def tv_remote(word):
#     shift, kb = coords["↑"], 0
#     moves, current = 0, (0, 0)
#     for char in word:
#         target, switch = coords[char.lower()], get_switch(kb, char)
#         if switch:
#             moves, current, kb = moves + switch-1 + distance(current, shift), shift, (kb + switch) % 3
#         moves, current = moves + distance(current, target), target
#     return moves
#
# kb1 = ("abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/", "↑ ")
# kb3 = ("^~?!'\"()", "-:;+&%*=", "<>€£$¥¤\\", "[]{},.@§", "#¿¡   _/")
# coords = {c: (line.index(c), y) for kb in (kb1, kb3) for y, line in enumerate(kb) for c in line}
#
# def get_switch(kb, char):
#     target = (0 if char.islower() else 1 if char.isupper()
#               else (kb != 2 and kb) if char.isdecimal() else 2 if char not in ".@_/↑ " else kb)
#     return (target - kb) % 3
#
# def distance(pos1, pos2):
#     d0, d1 = abs(pos2[0] - pos1[0]), abs(pos2[1] - pos1[1])
#     return 1 + min(d0, 8 - d0) + min(d1, 6 - d1)


"""[-2:]+[:-2]"""
# def tv_remote(words):
#     kpad=['abcde123fghij456klmno789pqrst.@0uvwxyz_/○ ☺☺☺☺☺',
#     'ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/○ ☺☺☺☺☺☺',
#     '^~?!\'"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡☺☺☺_/○ ☺☺☺☺☺☺']
#     lenght, coord = [0 for _ in range(2)]
#     lst=list(kpad[0])
#     for i in words:
#         while kpad[0].find(i)==-1:
#             lenght,coord = calculate(lst,'○',lenght,coord)
#             kpad=kpad[-2:]+kpad[:-2]
#             lst=list(kpad[0])
#         lenght,coord = calculate(lst,i,lenght,coord)
#     return lenght
#
# def calculate(lst, i, lenght, coord):
#     x=abs(lst.index(i)%8-coord%8)
#     y=abs(lst.index(i)//8-coord//8)
#     lenght += min(x,8-x)+min(y,6-y)+1
#     return [lenght,lst.index(i)]