from sys import stdin


n = int(stdin.readline())
buses = list(map(int, stdin.readline().split()))
h = dict()
maxTime = 0
for i in range(n):
    if buses[i] in h:
        maxTime = max(maxTime, i - h[buses[i]])
        h[buses[i]] = i
    else:
        h[buses[i]] = i
print(maxTime)
