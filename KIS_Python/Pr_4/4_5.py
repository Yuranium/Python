import math


def main(n):
    return (
        -0.20
        if n == 0
        else (-0.18 if n == 1 else
              (85 * main(n - 2) + math.exp(main(n - 1) + 1
                                           + (main(n - 2)) ** 3) ** 3))
    )


print('%.2e' % main(9))
print('%.2e' % main(5))
print('%.2e' % main(7))
print('%.2e' % main(2))
print('%.2e' % main(6))
