from math import log2


def main(x):
    return (27 * x ** 2 - 12 * (95 * x ** 2 + x ** 3) ** 3 if x < 100 else
            (x ** 2 + (39 * x ** 2 + 0.08)
            / 10 + (log2(x)) ** 6) if 100 <= x < 173 else
            (11 * (94 * x ** 2 + x + 47 * x ** 3) ** 7 if 173 <= x < 258 else
            22 * x ** 3 + 1))


print('%.2e' % main(243))
print('%.2e' % main(115))
print('%.2e' % main(186))
print('%.2e' % main(242))
print('%.2e' % main(221))
print('%.2e' % main(157))
