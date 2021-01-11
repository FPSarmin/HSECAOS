f0 = 1
f1 = 1
n = int(input())
i = 2
while f1 < n:
    (f1, f0) = (f0, f1)
    f1 += f0
    i += 1
    if f1 > n:
        print(-1)
        break
    if f1 == n:
        print(i)
