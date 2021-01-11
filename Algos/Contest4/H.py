from sys import stdin


n = int(stdin.readline())
spells = []
sumDam = 0
for _ in range(n):
    spells.append(list(map(int, stdin.readline().split())))
    sumDam += spells[-1][-1]
x = int(stdin.readline())
dp = [0] + [1000000000 for _ in range(x + sumDam)]
for i in range(n):
    for j in range(x + sumDam + 1):
        dp[j] = min(dp[j], dp[j - spells[i][-1]] + spells[i][0])
print(min(dp[x:]))
