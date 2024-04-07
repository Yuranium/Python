from math import log2


def main(x: int) -> float:
    conditions = {
        x < 100: lambda x: 27 * x ** 2 - 12 * (95 * x ** 2 + x ** 3) ** 3,
        100 <= x < 173: lambda x: x ** 2 + (39 * x ** 2 + 0.08)
        / 10 + (log2(x)) ** 6,
        173 <= x < 258: lambda x:
        11 * (94 * x ** 2 + x + 47 * x ** 3) ** 7
    }
    for condition, expression in conditions.items():
        if condition:
            return expression(x)
    return 22 * x ** 3 + 1
