import math


def main(n):
    conditions = {
        n == 0: lambda n: -0.20,
        n == 1: lambda n: -0.18
    }

    for condition, expression in conditions.items():
        if condition:
            return expression(n)

    return 85 * main(n - 2) + math.exp(main(n - 1) + 1
                                       + (main(n - 2)) ** 3) ** 3


print('%.2e' % main(9))
print('%.2e' % main(5))
print('%.2e' % main(7))
print('%.2e' % main(2))
print('%.2e' % main(6))
