a = list(map(int, input().split()))
max = sorted(a, reverse=True)[0]
count = a.count(max)
ind = a.index(max)
for i in range(count - 1):
    ind = a.index(max, ind + 1)
print(max, ind)
