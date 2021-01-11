a = list(map(int, input().split()))
min = 0
for i in a:
    if (min == 0 and i > 0) or (0 < i < min):
        min = i
print(min)
