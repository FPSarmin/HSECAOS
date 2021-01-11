from sys import stdin


def check(a, m, n):
    lines = 0
    i = 0
    while i < len(a):
        temp = 0
        while i < len(a) and temp + len(a[i]) <= m:
            temp += len(a[i])
            temp += 1
            i += 1
        lines += 1
        if i < len(a) and m < len(a[i]):
            return True
    return lines > n


def binSearch(a, n):
    L = 0
    R = 10**6
    while L < R - 1:
        M = (L + R) // 2
        temp = check(a, M, n)
        if temp:
            L = M
        else:
            R = M
    return R


congr = stdin.readline().split()
n = int(stdin.readline())
print(binSearch(congr, n))
