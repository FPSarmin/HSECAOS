n = int(input())
count = 1
i = 1
amount = 0
while i <= n:
    temp = i
    temp_num = str(i % 10)
    while temp >= 10:
        temp_num += str(i % (10**(count + 1)) // 10**count)
        temp //= 10
        count += 1
    count = 1
    if i == int(temp_num):
        amount += 1
    i += 1
print(amount)
