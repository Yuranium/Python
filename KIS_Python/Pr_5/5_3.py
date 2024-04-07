import math


def main(y, x):
    n = 5
    sum_val = 0
    i = 1
    while i <= n:
        sum_val += (13 + y[n - math.ceil(i / 4)] ** 3 + x[i - 1] ** 2) ** 6
        i += 1
    return 16 * sum_val


print('%.2e' % main([-0.4, 0.46, -0.95, -0.21, 0.56], [0.88, -0.77, 0.9, -0.98, 0.15]))
