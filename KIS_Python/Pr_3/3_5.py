from math import ceil
from functools import reduce


def main(n: int, m: int, z: float) -> float:
    return reduce(
        lambda acc, j: acc + reduce(
            lambda acc_inner, c: acc_inner +
            ((ceil(36 * z - 59 * z ** 2))**6 +
             ((j ** 2 + 60 * c ** 3) ** 2) / 79),
            range(1, n + 1), 0),
        range(1, m + 1), 0)


print('%.2e' % main(6, 5, -0.25))
print('%.2e' % main(4, 3, -0.69))
print('%.2e' % main(8, 4, 0.42))
print('%.2e' % main(3, 2, -0.09))
print('%.2e' % main(7, 4, 0.4))

# from math import ceil
#
#
# def main(n: int, m: int, z: float, j=1, c=1, f=0) -> float:
#     if j > m:
#         return f
#     if c > n:
#         return main(n, m, z, j + 1, 1, f)
#     return main(n, m, z, j, c + 1, f +
#                 ((ceil(36 * z - 59 * z ** 2)) ** 6
#                  + ((j ** 2 + 60 * c ** 3) ** 2) / 79))
