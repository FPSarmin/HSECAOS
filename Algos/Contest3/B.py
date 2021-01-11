from sys import stdin


def binSearch(a, x):
    L = -1
    R = len(a)
    while L < R - 1:
        M = (L + R) // 2
        if a[M] <= x:
            L = M
        else:
            R = M
    return L if a[L] == x else -1


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
mNums = list(map(int, stdin.readline().split()))
sum = 0
for i in range(m):
    sum += binSearch(a, mNums[i])
print(sum)
