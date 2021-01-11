a = list(map(int, input().split()))
if len(a) <= 1:
    print(*a)
else:
    if a[0] < a[1]:
        minInd = 0
        maxInd = 1
    else:
        minInd = 1
        maxInd = 0
    for i in range(len(a)):
        if a[i] < a[minInd]:
            minInd = i
        if a[i] > a[maxInd]:
            maxInd = i
    a[minInd], a[maxInd] = a[maxInd], a[minInd]
    print(*a)
