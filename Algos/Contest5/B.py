from sys import stdin


n, m = map(int, stdin.readline().split())
dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        temp = max(i, j) // 2 + max(i, j) % 2 - 1
        for k in range(max(i, j) - 1, max(i, j) // 2 + max(i, j) % 2 - 1, -1):
            if (i > k > i // 2 + i % 2 - 1 and not dp[k][j]) or\
                    (j > k > i // 2 + i % 2 - 1 and not dp[i][k]):
                dp[i][j] = 1

print('Max' if dp[-1][-1] else 'Igor')
