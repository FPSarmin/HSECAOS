from sys import stdin
import heapq


n = int(stdin.readline())
time = list(map(int, stdin.readline().split()))
tills = [[0, i] for i in range(n)]
m = int(stdin.readline())
amount = list(map(int, stdin.readline().split()))
for i in range(m):
    temp = heapq.heappop(tills)
    print(temp[1] + 1, end=" ")
    temp[0] += time[temp[1]] * amount[i]
    heapq.heappush(tills, temp)

