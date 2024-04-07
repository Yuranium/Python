import math


def main(y, x):
    return 16 * sum((13 + y[5 - math.ceil(i / 4)] ** 3
                     + x[i - 1] ** 2) ** 6 for i in range(1, 6))


print('%.2e' % main([-0.4, 0.46, -0.95, -0.21, 0.56], [0.88, -0.77, 0.9, -0.98, 0.15]))
