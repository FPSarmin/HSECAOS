m = int(input())
n = 1
count = 0
while n != 0:
    n = int(input())
    if n > m:
        count += 1
    m = n
print(count)
