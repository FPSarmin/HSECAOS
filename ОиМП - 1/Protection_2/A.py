n, m = map(int, input().split())
k, p = map(int, input().split())
for i in range(k, n + 1, k):
    for j in range(p, m + 1, p):
        cabnum = str(j)
        if j < 10:
            cabnum = '0' + str(j)
        print(str(i)+cabnum)
