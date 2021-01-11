a = list(map(int, input().split()))
b = []
for i in range(1, len(a)):
    if (a[i] > 0 and a[i - 1] > 0) or (a[i] < 0 and a[i - 1] < 0):
        b.append(a[i - 1])
        b.append(a[i])
        i += 1
        break
print(*b)
