import math


def main(n):
    if n == 0:
        return -0.20
    elif n == 1:
        return -0.18
    elif n >= 2:
        return 85 * main(n - 2) + (math.exp(main(n - 1)
                                            + 1 + (main(n - 2)) ** 3)) ** 3


print('%.2e' % main(9))
print('%.2e' % main(5))
print('%.2e' % main(7))
print('%.2e' % main(2))
print('%.2e' % main(6))