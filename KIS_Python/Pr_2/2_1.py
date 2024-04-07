from math import sqrt, log2


def main(x):
    if x < 100:
        return 27 * x ** 2 - 12 * (95 * x ** 2 + x ** 3) ** 3
    elif 100 <= x < 173:
        return x ** 2 + (39 * x ** 2 + 0.08) / 10 + (log2(x)) ** 6
    elif 173 <= x < 258:
        return 11 * (94 * x ** 2 + x + 47 * x ** 3) ** 7
    else:
        return 22 * x ** 3 + 1


print(main(186))
