from sys import stdin


n, a, b = map(int, stdin.readline().split())
game = n
dp = [0 for __ in range(n + 1)]
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = 0
    if (i - 1 >= 0 and dp[i - 1] == 0) or \
            (i - a >= 0 and dp[i - a] == 0)\
            or (i - b >= 0 and dp[i - b] == 0):
        dp[i] = 1
print(1 if dp[n] == 1 else 2)
