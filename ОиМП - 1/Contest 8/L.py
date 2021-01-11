dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
dist.sort()
cost.sort()
sum = 0
for i in range(len(dist)):
    sum += dist[-i - 1] * cost[i]
print(sum)
