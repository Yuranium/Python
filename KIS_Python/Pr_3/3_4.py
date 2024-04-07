from math import ceil


def main(n, m, z):
    f = 0
    j = 1
    while j <= m:
        c = 1
        while c <= n:
            f += ((ceil(36 * z - 59 * z ** 2)) ** 6
                  + ((j ** 2 + 60 * c ** 3) ** 2) / 79)
            c += 1
        j += 1
    return f
