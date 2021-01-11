n = 1
count = 1
max = 0
while n != 0:
    n = int(input())
    if n == max:
        count += 1
    if n > max:
        max = n
        count = 1
print(count)
