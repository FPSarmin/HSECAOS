a = list(map(int, input().split()))
max = a[0]
ind = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        ind = i
print(max, ind)
