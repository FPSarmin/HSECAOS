from sys import stdin


n = int(stdin.readline())
ways = [0 for _ in range(n)]
dp = [[10**9 for _ in range(1 << n)] for __ in range(n)]
for i in range(n):
    ways[i] = list(map(int, stdin.readline().split()))
for mask in range(1, 2**n):
    cities = []
    amount = 0
    for i in range(n):
        if mask & (1 << i):
            amount += 1
            cities.append(i)
    if amount == 1:
        dp[cities[0]][mask] = ways[0][cities[0]]
    for i in range(amount):
        prev = cities[:i] + cities[i + 1:]
        prevmask = mask - (1 << cities[i])
        for p in prev:
            dp[cities[i]][mask] = min(dp[cities[i]][mask],
                                      dp[p][prevmask] + ways[p][cities[i]])
print(dp[0][-1])
