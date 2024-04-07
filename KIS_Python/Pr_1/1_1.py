import math


def main(y, x):
    return ((0.17 + math.pow(x, 2) - 26 * math.pow(y, 6))
            / math.pow((13 + math.pow(y, 3) + math.pow(x, 2)), 4)
            + (((math.pow(y, 2) / 60 + (x / 37)) ** 4) / 18)
            / math.pow((72 + math.pow(x, 3) + 94 * y), 6))


print('%.2e' % main(0.86, -0.28))
