from sys import stdin


A, B = stdin.readline().split()
dp = [[1000**2 + 1 for _ in range(len(B) + 1)] for __ in range(len(A) + 1)]
w = 0
for i in range(len(A) + 1):
    for j in range(len(B) + 1):
        if i == 0:
            dp[i][j] = j
            continue
        if j == 0:
            dp[i][j] = i
            continue
        w = 0 if A[i - 1] == B[j - 1] else 1
        dp[i][j] = min([dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1, dp[i - 1][j - 1] + w])
print(dp[-1][-1])
