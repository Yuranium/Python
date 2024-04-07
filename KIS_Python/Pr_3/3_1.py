from math import ceil


def main(n, m, z):
    sum = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sum += ((ceil(36 * z - 59 * z ** 2)) ** 6
                    + ((i ** 2 + 60 * j ** 3) ** 2) / 79)
    return sum
