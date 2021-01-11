a = list(map(int, input().split()))
zero = a.index(0)
for i in range(len(a)):
    if i > zero and a[i] != 0:
        a[i], a[zero] = a[zero], a[i]
        zero += 1
print(*a)
