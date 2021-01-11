s, n = map(int, input().split())
a = [0] * 1001
count = 0
for i in range(n):
    temp = int(input())
    a[temp] += 1
for i in range(len(a)):
    while a[i] > 0 and s >= 0:
        count += 1
        s -= i
        a[i] -= 1
if s < 0:
    count -= 1
print(count)