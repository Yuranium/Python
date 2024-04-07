import math


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def main(N):
    E = { math.ceil(v / 7) + v for v in N if -78 < v < 66 }
    Omega = N.union(E)
    H = {e * w for e in E for w in Omega if e >= w}
    a = len(Omega) * len(H) + prod([eta % 2 for eta in H])
    return a
