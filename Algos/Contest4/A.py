from sys import stdin

n, m = map(int, stdin.readline().split())
way = list(map(int, stdin.readline().split()))
currsum = 1
for i in range(1, n):
    if i < m:
        way[i] = currsum * way[i]
        currsum += way[i]
    else:
        way[i] = currsum * way[i]
        currsum -= way[i - m]
        currsum += way[i]

print(way[n-1] % 1000000007)
