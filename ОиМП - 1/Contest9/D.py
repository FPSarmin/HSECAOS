a = list(map(int, input().split()))
b = set({})
for i in range(len(a)):
    if a[i] in b:
        print("YES")
    else:
        print("NO")
        b.add(a[i])
