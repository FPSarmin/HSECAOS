from sys import stdin


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
prefSum = [0 for i in range(n)]
prefSum[0] = nums[0]
for i in range(1, n):
    prefSum[i] = nums[i] + prefSum[i - 1]
k = int(stdin.readline())
for i in range(k):
    l, r = map(int, stdin.readline().split())
    if l > 0:
        print(prefSum[r] - prefSum[l - 1])
    else:
        print(prefSum[r])
