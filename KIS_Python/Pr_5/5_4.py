import math


def main(y, x, n=5, i=1, sum=0):
    if i > n:
        return 16 * sum
    else:
        sum += (13 + y[n - math.ceil(i / 4)] ** 3 + x[i - 1] ** 2) ** 6
        return main(y, x, n, i + 1, sum)


print('%.2e' % main([-0.4, 0.46, -0.95, -0.21, 0.56], [0.88, -0.77, 0.9, -0.98, 0.15]))
