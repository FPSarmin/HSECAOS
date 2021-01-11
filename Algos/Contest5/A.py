from sys import stdin


n = int(stdin.readline())
dp = [10**7 for _ in range(n + 1)]
dp[1] = 0
for i in range(1, n):
        d = dp[i] + 1
        if i + 1 <= n:
            dp[i + 1] = min(d, dp[i + 1])
        if i * 2 <= n:
            dp[i * 2] = min(d, dp[i * 2])
        if i * 3 <= n:
            dp[i * 3] = min(d, dp[i * 3])
print(dp[n])
