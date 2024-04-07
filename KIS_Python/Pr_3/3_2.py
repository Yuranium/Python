from math import sin


def main(b, n, m):
    temp = 0
    for k in range(1, m + 1):
        for i in range(1, n + 1):
            for c in range(1, b + 1):
                temp += 40 * (sin(93 - (c ** 2)
                                  / 95 - k ** 3)) ** 7 - k ** 3 - i
    return temp
