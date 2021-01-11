from sys import stdin


n = int(stdin.readline())
arr = [i for i in range(1, n + 1)]

j = 0
for i in range(n):
    m = len(arr) // 2 + (j*(-1)**i) * (-1)**n
    arr[m] = n - i
    if i % 2 == 0:
        j += 1
print(*arr)




