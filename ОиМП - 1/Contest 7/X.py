a = list(map(int, input().split()))
maxCount = 1
maxNum = a[0]
for i in range(len(a)):
    count = a.count(a[i])
    if count > maxCount:
        maxCount = count
        maxNum = a[i]
print(maxNum)
