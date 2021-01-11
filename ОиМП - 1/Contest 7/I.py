a = list(map(int, input().split()))
min = 0
for i in a:
    if (min == 0 and i % 2 == 1) or (i < min and i % 2 == 1):
        min = i
print(min)
