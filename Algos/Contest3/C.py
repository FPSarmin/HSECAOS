from sys import stdin


def binSearch(L, R, x, y, n):
    while L < R - 1:
        M = (L + R) // 2
        if M // x + M // y < n:
            L = M
        else:
            R = M
    return R


n, x, y = map(int, stdin.readline().split())
print(binSearch(0, n * max(x, y), x, y, n))
