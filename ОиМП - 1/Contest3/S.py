n = int(input())
temp = n
count = 1
print(n % 10, end="")
while temp >= 10:
    print(n % (10**(count + 1)) // 10**count, end="")
    temp //= 10
    count += 1
