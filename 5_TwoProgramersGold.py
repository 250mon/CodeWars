import math
"""
[a, b, c, ..., x, y, z]
- choose the largest of a,b,y,z
- if a is the largest, take it (same for z)
- if b is the largest, compare (z->b) and (a->c)
  if z->b is larger, take z. Otherwise, take a (same for y)
"""
def distribution_of2(gold):
    a = []
    b = []
    turn = a
    for i in range(len(gold)):
        if len(gold) == 1:
            turn.append(gold.pop())
            break

        subgrp_len = 4 if len(gold) > 3 else len(gold)
        subidx = subgrp_len // 2
        subgrp = gold[:subidx] + gold[-1 * subidx:]
        max_val = max(subgrp)
        max_idx = subgrp.index(max_val)
        max_idx = max_idx if max_idx < math.ceil(subgrp_len / 2) else max_idx - subgrp_len
        pick_idx = max_idx
        if max_idx == 1:
            if (max_val + gold[-1]) >= (gold[0] + gold[2]): pick_idx = -1
            else: pick_idx = 0
        elif max_idx == -2:
            if (max_val + gold[0]) >= (gold[-1] + gold[-3]): pick_idx = 0
            else: pick_idx = -1

        turn.append(gold.pop(pick_idx))

        if turn == a: turn = b
        else: turn = a

    print(a)
    print(b)
    return sum(a), sum(b)


def distribution_of(gold):
    n = [*gold]
    for s in range(2, len(gold)+1):
        m = [min(n[i:i+2]) for i in range(len(n)-1)]
        n = [sum(gold[i:i+s])-v for i, v in enumerate(m)]
    return (*n,*m)


if __name__ == '__main__':
    gold = [4, 7, 2, 9, 5, 2]
    gold2 = [140, 649, 340, 982, 105, 86, 56, 610, 340, 879]
    gold3 = [782, 26, 417, 700, 985, 258, 120, 637, 478, 510] # 2782, 2131
    gold4 = [32, 103, 918, 955, 666, 548, 310, 898, 436, 680, 716, 886]  # 4070, 3078
    print(distribution_of(gold3))