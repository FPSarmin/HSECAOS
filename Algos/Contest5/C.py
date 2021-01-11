from sys import stdin


def tower(amount, prev):
    if dp[amount][prev] != -1:
        return dp[amount][prev]
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    suma = 0
    for i in range(1, prev + 1):
        dp[amount - i][i] = tower(amount - i, i) % 1000000007
        suma += dp[amount - i][i] % 1000000007
    return suma % 1000000007


n = int(stdin.readline())
dp = [[-1 for _ in range(n + 1)] for __ in range(n + 1)]
print(tower(n, n))
