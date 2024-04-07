from math import *


def main(y, x):
    return ((0.17 + x ** 2 - 26 * y ** 6) / (13 + y ** 3 + x ** 2)**4
            + ((((y ** 2 / 60) + (x / 37)) ** 4)
               / (18 * (72 + x ** 3 + 94 * y) ** 6)))

# from math import *
#
#
# def main(y, x):
#     result = ((0.17 + pow(x, 2) - 26 * pow(y, 6)) / pow((13 + pow(y, 3) + pow(x, 2)), 4)
#               + (pow(((pow(y, 2) / 60) + (x / 37)), 4)
#                  / (18 * pow((72 + pow(x, 3) + 94 * y), 6))))
#     return result
