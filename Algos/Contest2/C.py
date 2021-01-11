from sys import stdin
import heapq


n, k = map(int, stdin.readline().split())
aZero, x, y = map(int, stdin.readline().split())
a = [aZero]
arr = list()
prev = aZero
sum = -1 if k > 1 else aZero
if k == 1:
    heapq.heappop(a)
for i in range(1, n):
    prev = (prev * x + y) % (10 ** 9 + 7)
    heapq.heappush(a, prev)
    if i + 1 < k:
        sum -= 1
    else:
        if len(a) > k:
            heapq.heappop(a)
        sum += a[0]
print(sum)