from sys import stdin


A = stdin.readline().strip()
B = stdin.readline().strip()
if len(A) < len(B):
    A, B = B, A
dp = [[[0, 1] for _ in range(len(B) + 1)] for __ in range(2)]
dp[1] = [[0, 0] for _ in range(len(B) + 1)]
dp[1][0] = [0, 1]
for i in range(1, len(A) + 1):
    dp[1][0] = [0, 1]
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[1][j] = [dp[0][j - 1][0] + 1, dp[0][j - 1][1]]
        else:
            if dp[0][j][0] > dp[1][j - 1][0]:
                dp[1][j] = dp[0][j]
            elif dp[0][j][0] < dp[1][j - 1][0]:
                dp[1][j] = dp[1][j - 1]
            else:
                dp[1][j] = [dp[1][j - 1][0], dp[0][j][1] + dp[1][j - 1][1]]
                dp[1][j][1] -= dp[0][j - 1][1] if\
                    dp[0][j - 1][0] == dp[1][j][0] else 0
        dp[1][j][1] %= 1000000007
    dp[0] = dp[1]
    dp[1] = [[0, 0] for _ in range(len(B) + 1)]
    dp[1][0] = [0, 1]

print(dp[0][-1][-1] % 1000000007 if dp[0][-1][0] != 0 else 0)
