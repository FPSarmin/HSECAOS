n = int(input())
sum = 1
fact = 1
for i in range(2, n + 1):
    fact *= i
    sum += fact
print(sum)
