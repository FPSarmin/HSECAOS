from sys import stdin


n = int(stdin.readline())
aZero, x, y = map(int, stdin.readline().split())
a = [0 for _ in range(11)]
for i in range(n):
    a[aZero] += 1
    aZero = (aZero * x + y) % 11
prefix_sum = 0
sum = 0
for i in range(11):
    if prefix_sum == 0 and a[i] != 0:
        prefix_sum += 1
        a[i] -= 1
    if a[i] == 0:
        continue
    temp = i * ((2 * prefix_sum + a[i] - 1) * a[i] // 2)
    sum += temp
    prefix_sum += a[i]
print(sum)
