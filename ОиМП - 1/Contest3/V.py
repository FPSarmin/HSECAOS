n = int(input())
count = 1
bigger = True
max_count = 1
temp = n
while n != 0:
    n = int(input())
    if n > temp and n != 0:
        if bigger:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 2
            bigger = True
    elif n < temp and n != 0:
        if not bigger:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 2
            bigger = False
    elif n == temp:
        max_count = max(max_count, count)
        count = 1
    temp = n
max_count = max(max_count, count)
print(max_count)
