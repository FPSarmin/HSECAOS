from sys import stdin


n = int(stdin.readline())
commands = set()
for _ in range(n):
    commands.add(stdin.readline().strip())
dComma = stdin.readline().strip()
cN = len(dComma)
dp = [0 for _ in range(cN)]
for i in range(cN):
    for j in range(i + 1):
        temp = dComma[j:i + 1]
        if j == 0:
            dp[i] = 1 if temp in commands else 0
            continue
        dp[i] += dp[j - 1] % 1000000007 if temp in commands else 0
print(dp[cN - 1] % 1000000007)
