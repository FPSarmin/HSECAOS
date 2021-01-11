from sys import stdin
import heapq


n = int(stdin.readline())
aZero, x, y = map(int, stdin.readline().split())
a = [(0, aZero)]
for i in range(1, n):
    aZero = (aZero * x + y) % (10**9 + 7)
    heapq.heappush(a, (i, aZero))
sum = 0
while len(a) > 0:
    if len(a) >= 3:
        if a[1][0] < a[0][0] and a[2][0] < a[0][0]:
            sum -= 1
        elif a[1][0] > a[0][0] and (a[1][0] < a[2][0] or a[2][0] < a[0][0]):
            sum += a[1][0]
        else:
            sum += a[2][0]
        heapq.heappop(a)
        continue
    else:
        if len(a) == 2:
            if a[1][0] < a[0][0]:
                sum -= 1
            else:
                sum += a[1][0]
            heapq.heappop(a)
        if len(a) == 1:
            sum -= 1
            heapq.heappop(a)
print(sum)
