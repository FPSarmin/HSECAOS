from sys import stdin
from math import sqrt


def dist(x, y, x1, y1):
    return sqrt((x - x1)**2 + (y - y1)**2)


def check(a, x, y):
    sum = 0
    for i in range(len(a)):
        temp = dist(a[i][0], a[i][1], x, y)
        sum += temp
    return sum


def ternSearchY(a, x):
    L = -1000
    R = 1000
    eps = 10**(-8)
    while R - L > eps:
        m1 = L + (R - L) / 3
        m2 = R - (R - L) / 3
        if check(a, x, m1) > check(a, x, m2):
            L = m1
        else:
            R = m2
    return R


def ternSearch(a):
    L = -1000
    R = 1000
    eps = 10**(-9)
    while R - L > eps:
        m1 = L + (R - L) / 3
        m2 = R - (R - L) / 3
        if check(a, m1, ternSearchY(a, m1)) > check(a, m2, ternSearchY(a, m2)):
            L = m1
        else:
            R = m2
    return R, ternSearchY(a, R)


n = int(stdin.readline())
a = []
for i in range(n):
    temp = list(map(float, stdin.readline().split()))
    a.append(temp)
answer = ternSearch(a)
print(f"{answer[0]:.{6}f} {answer[1]:.{6}f}")
