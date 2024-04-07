def main(h: str):
    v = int(h, 16)
    c1 = v & 0b1111111111
    c3 = (v >> 12) & 0b111111111
    c4 = (v >> 21) & 0b1111111
    c5 = (v >> 28) & 0b111111
    d = c1 | (c5 << 10) | (c3 << 17) | (c4 << 26)
    return str(hex(d))


# Проверка
print(main('0xa19bac8f'))  # '0x3374288f'
print(main('0x85fef15c'))  # '0xbfde215c'
print(main('0x1fc4dcc1d'))  # '0x189b87c1d'
print(main('0x151d1d103'))  # '0x3a3a5503'
