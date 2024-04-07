import math


def main(n, m, z):
    summ = sum(((math.ceil(36 * z - 59 * z ** 2)) ** 6
                + ((i ** 2 + 60 * c ** 3) ** 2) / 79)
               for i in range(1, m + 1)
               for c in range(1, n + 1)
               )
    return summ
