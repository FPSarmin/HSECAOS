a = list(map(int, input().split()))
b = []
for i in a:
    if not i % 2:
        b.append(i)
print(*b)
