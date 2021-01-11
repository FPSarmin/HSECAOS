from sys import stdin
from math import sqrt


def dist(x, y, x1, y1):
    return sqrt((x - x1)**2 + (y - y1)**2)


def check(a, x):
    sum = 0
    for i in range(len(a)):
        temp = dist(a[i][0], a[i][1], x, 0)
        sum += temp
    return sum


def ternSearch(a):
    L = -1000
    R = 1000
    eps = 10**(-8)
    while R - L > eps:
        m1 = L + (R - L) / 3
        m2 = R - (R - L) / 3
        if check(a, m1) > check(a, m2):
            L = m1
        else:
            R = m2
    return R


n = int(stdin.readline())
a = []
for i in range(n):
    temp = list(map(float, stdin.readline().split()))
    a.append(temp)
print(f"{ternSearch(a):.{4}f}")
