n = int(input())
sum = ((1 + n) * n) // 2
for i in range(1, n):
    temp = int(input())
    sum -= temp
print(sum)
