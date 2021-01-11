size = int(input())
a = list(map(int, input().split()))
a.sort(key=lambda x: x - size)
count = 0
for i in range(len(a)):
    if a[i] < 0:
        continue
    if a[i] - size >= 3 or (count == 0 and a[i] == size):
        count += 1
        size = a[i]
    else:
        continue
print(count)
