a = list(map(int, input().split()))
b = []
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        b.append(a[i])
print(*b)
