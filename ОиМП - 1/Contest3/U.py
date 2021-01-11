n = int(input())
count = 1
max_count = 1
temp = n
if n == 0:
    print(0)
else:
    while n != 0:
        n = int(input())
        if n == temp:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
        temp = n
    print(max_count)
