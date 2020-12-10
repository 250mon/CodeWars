import string


keypad = {
    1: [
        list('abcde123'),
        list('fghij456'),
        list('klmno789'),
        list('pqrst.@0'),
        list('uvwxyz_/'),
        ['aA#', ' ', '', '', '', '', '', ''],
    ],
    3: [
        ['^', '~', '?', '!', "'", '"', '(', ')'],
        ['-', ':', ';', '+', '&', '%', '*', '='],
        ['<', '>', '€', '£', '$', '¥', '¤', '\\'],
        ['[', ']', '{', '}', ',', '.', '@', '§'],
        ['#', '¿', '¡', '', '', '', '_', '/'],
        ['aA#', ' ', '', '', '', '', '', ''],
    ]
}


def tv_remote(words):
    curr_mode, next_mode = 1, 1
    curr_ch = 'a'
    total_key_strokes = 0
    word_list = list(words)
    for next_ch in word_list:
        key_strokes = 0

        next_mode = mode_for(next_ch, curr_mode)
        if curr_mode != next_mode:
            key_strokes += change_mode_key_strokes(curr_mode, next_mode, curr_ch)
            curr_mode = next_mode
            curr_ch = 'aA#'

        key_strokes += distance(curr_mode, curr_ch, next_ch)
        # pressing ok
        key_strokes += 1
        curr_ch = next_ch
        total_key_strokes += key_strokes

    return total_key_strokes


def coordinate(mode, ch):
    for row_index, row in enumerate(keypad[mode]):
        if ch in row:
            col_index = row.index(ch)
            return col_index, row_index


def distance(mode, curr_ch, next_ch):
    if mode == 2:
        mode = 1
        if curr_ch in string.ascii_uppercase: curr_ch = curr_ch.lower()
        if next_ch in string.ascii_uppercase: next_ch = next_ch.lower()
    x1, y1 = coordinate(mode, curr_ch)
    x2, y2 = coordinate(mode, next_ch)
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    dx, dy = dx if dx < 5 else 8 - dx, dy if dy < 4 else 6 - dy
    return dx + dy


def change_mode_key_strokes(cmode, nmode, cpos):
    dist = distance(cmode, cpos, 'aA#')
    if (okes := nmode - cmode) < 0:
        okes += 3
    return dist + okes


def mode_for(ch, cmode):
    if ch in list(' .@_/'):
        mode = cmode
    elif ch in string.ascii_lowercase:
        mode = 1
    elif ch in string.ascii_uppercase:
        mode = 2
    elif ch in string.digits:
        mode = 1 if cmode == 3 else cmode
    else:
        mode = 3

    return mode


if __name__ == '__main__':
    print(tv_remote("&wMI7b/ .N"))
    #print(tv_remote("R'MI7b/ .N"))
