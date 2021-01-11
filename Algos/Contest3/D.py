from sys import stdin


def countWoods(a, m, n):
    sum = 0
    for i in a:
        sum += i // m
    return sum >= n


def binSearch(a):
    L = 0
    R = sum(a) + 1
    temp = 0
    M = 0
    while L < R - 1:
        M = (L + R) // 2
        if countWoods(a, M, n):
            L = M
        else:
            R = M
    return L


n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
print(binSearch(a, n) if sum(a) >= n else 0)
