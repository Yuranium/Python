def main(y, x):
    temp1 = (0.17 + x ** 2 - 26 * y ** 6) / (13 + y ** 3 + x ** 2)**4
    temp2 = ((((y ** 2 / 60) + (x / 37)) ** 4) /
             (18 * (72 + x ** 3 + 94 * y) ** 6))
    return temp1 + temp2
