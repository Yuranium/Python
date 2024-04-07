import math


def main(y, x):
    return ((0.17 + x ** 2 - 26 * y ** 6) / (13 + y ** 3 + x ** 2)**4
            + ((((y ** 2 / 60) + (x / 37)) ** 4)
               / (18 * (72 + x ** 3 + 94 * y) ** 6)))

# import math
# import functools


# def main(y, x):
#     a = []
#     a.append((0.17 + x ** 2 - 26 * y ** 6) / (13 + y ** 3 + x ** 2) ** 4)
#     a.append((((y ** 2 / 60 + (x / 37)) ** 4) / 18)
#              / (72 + x ** 3 + 94 * y) ** 6)
#     return sum(a)
# def main(y, x):
#     a = [
#         (0.17 + x ** 2 - 26 * y ** 6) / (13 + y ** 3 + x ** 2) ** 4,
#         (((y ** 2 / 60 + (x / 37)) ** 4) / 18)
#         / (72 + x ** 3 + 94 * y) ** 6
#     ]
#     return sum(map(lambda x: x, a))
