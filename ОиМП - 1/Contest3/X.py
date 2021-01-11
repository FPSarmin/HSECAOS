n = 1
count = 0
sum = 0
sq_sum = 0
while n != 0:
    n = int(input())
    sum += n
    sq_sum += n**2
    count += 1
count -= 1
print(((sq_sum - sum**2 / count) / (count - 1)) ** 0.5)
