from sys import stdin


w, n = map(int, stdin.readline().split())
ropes = list(map(int, stdin.readline().split()))
dp = [-1 for _ in range(w + 2)]
dp[0] = 0
for i in range(n):
    for j in range(w - ropes[i], -1, -1):
        if dp[j] != -1 and dp[j + ropes[i]] == -1:
            dp[j + ropes[i]] = i
s = w
answer = []
if dp[w] == -1:
    print(-1)
else:
    while s > 0:
        answer.append(dp[s] + 1)
        s -= ropes[dp[s]]
    print(len(answer))
    print(*answer)
