from sys import stdin

n = int(stdin.readline())
k = list(map(int, stdin.readline().split()))
prefixSum = [k[0]] + [0 for _ in range(1, n)]
answer = 0
for i in range(1, n):
    prefixSum[i] = prefixSum[i - 1] + k[i]
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        answer += (k[i] * k[j] * (prefixSum[n - 1] - prefixSum[j]))\
                  % 1000000007
print(answer)
