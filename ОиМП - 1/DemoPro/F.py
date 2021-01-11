prev = int(input())
n = int(input())
if n != 0:
    count = 0
    next = 0
    while True:
        next = int(input())
        if next == 0:
            break
        if n > prev and n > next:
            count += 1
        prev, n = n, next
    print(count)
else:
    print(0)
