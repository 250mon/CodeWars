# >>> n = 255
# >>> f"{n:#x}"     '0xff'
# >>> f"{n:#02x}"   '0xff'
# >>> f"{n:#03x}"   '0xff'
# >>> f"{n:x}"      'ff'
# >>> f"{n:0x}"     'ff'
# >>> f"{n:03x}"    '0ff'
# >>> f"{n:04x}"    '00ff'
# >>> f"{n:4x}"     '  ff'
# >>> f"{n:*^9x}"   '***ff****'

def rgb(r, g, b):
    result = []
    for n in (r, g, b):
        if n > 255: n = 255
        elif n < 0: n = 0
        result.append(f"{n:02X}")
    return "".join(result)


"""format, min and max"""
# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


if __name__ == '__main__':
    print(rgb(-20,275,125))
