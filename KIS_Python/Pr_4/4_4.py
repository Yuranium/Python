import math


def main(n):
    match n:
        case 0:
            return -0.20
        case 1:
            return -0.18
        case _:
            return 85 * main(n - 2) + math.exp(main(n - 1) + 1
                                               + (main(n - 2)) ** 3) ** 3


print('%.2e' % main(9))
print('%.2e' % main(5))
print('%.2e' % main(7))
print('%.2e' % main(2))
print('%.2e' % main(6))
