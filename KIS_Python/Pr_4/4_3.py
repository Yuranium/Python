import math


def main(n):  # 3 способ
    values = [-0.20, -0.18]
    for i in range(2, n + 1):
        values.append(85 * main(n - 2) + math.exp(main(n - 1) + 1
                                                  + (main(n - 2)) ** 3) ** 3)
    return values[n]


print('%.2e' % main(9))
print('%.2e' % main(5))
print('%.2e' % main(7))
print('%.2e' % main(2))
print('%.2e' % main(6))
