n = int(input())
sum = 0
while True:
    sum += n % 10
    if n < 10:
        break
    n //= 10
print(sum)
