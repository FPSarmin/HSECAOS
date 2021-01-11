prev = int(input())
if prev != 0:
    n = int(input())
else:
    n = 0
prevcount = 0
count = 2
ishave = 0
min_dist = 0
while n != 0:
    next = int(input())
    if n > prev and n > next != 0:
        ishave += 1
        if (min_dist == 0 or min_dist > count - prevcount) and ishave > 1:
            min_dist = count - prevcount
        prevcount = count
    (prev, n) = (n, prev)
    (n, next) = (next, n)
    count += 1
if ishave > 1:
    print(min_dist)
else:
    print(0)
