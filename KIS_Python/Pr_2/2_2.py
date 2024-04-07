import math


def main(x):
    result = (
        (27 * x ** 2 - 12 * (95 * x ** 2 + x ** 3) ** 3) if x < 100
        else ((x ** 2, (39 * x ** 2 + 0.08) / 10 + (math.log2(x)) ** 6)[x < 150]
              if 100 <= x < 173
              else (11 * (94 * x ** 2 + x + 47 * x ** 3) ** 7))
        if 173 <= x < 258
        else (22 * x ** 3 + 1))
    if x >= 258:
        return result
    return main(x + 1)
