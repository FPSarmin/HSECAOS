from sys import stdin


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
h = [[] for _ in range(n)]
for i in range(n):
    h[nums[i] % n].append(nums[i])
ans = 0
for i in range(n):
    ans += abs(len(h[i]) - 1)
ans = (1 - ans / (2*n - 2)) * 100
print(ans)
