from sys import stdin


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
dp = [0 for _ in range(n)]
p = [0 for _ in range(n)]
for i in range(n):
    dp[i] = 1
    p[i] = -1
    for j in range(i):
        if a[j] <= a[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                p[i] = j
ind = 0
for _ in range(n):
    ind = ind if dp[ind] > dp[_] else _
print(dp[ind])
l = dp[ind]
answer = []
while l > 0:
    answer.append(a[ind])
    ind = p[ind]
    l -= 1
answer.reverse()
print(*answer)
