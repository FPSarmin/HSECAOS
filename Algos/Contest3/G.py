from sys import stdin
from math import sqrt


def dist(x, y, x1, y1):
    return sqrt((x - x1)**2 + (y - y1)**2)


def ternSearch(y, v1, v2):
    L = 0
    R = 1
    eps = 10**(-8)
    while R - L > eps:
        m1 = L + (R - L) / 3
        m2 = R - (R - L) / 3
        if dist(0, 0, m1, y) / v1 + dist(m1, y, 1, 1) / v2 >\
                dist(0, 0, m2, y) / v1 + dist(m2, y, 1, 1) / v2:
            L = m1
        else:
            R = m2
    return R


y, v1, v2 = map(float, stdin.readline().split())
print(f"{ternSearch(y, v1, v2):.{6}f}")
