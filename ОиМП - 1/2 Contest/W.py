l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
is1 = 1
is2 = 2
is3 = 3
if l2 < l1 or l3 < l1:
    if l3 < l1:
        (is3, is1) = (is1, is3)
        (l1, l3) = (l3, l1)
        (r1, r3) = (r3, r1)
    if l2 < l1:
        (is2, is1) = (is1, is2)
        (l1, l2) = (l2, l1)
        (r1, r2) = (r2, r1)
if l3 < l2:
    (is3, is2) = (is2, is3)
    (l2, l3) = (l3, l2)
    (r2, r3) = (r3, r2)
answer = 0
if (l2 <= r1 and l3 <= r2) or r1 >= l3:
    print(0)
else:
    if l3 - r1 <= r2 - l2:
        answer += 10**(is2 - 1)
    if r1 >= l2 or l2 - r1 <= r3 - l3:
        answer += 10**(is3 - 1)
    if r2 >= l3 or l3 - r2 <= r1 - l1:
        answer += 10**(is1 - 1)
    if answer != 0:
        if answer % 10 == 1:
            print(1)
        elif answer // 10 % 10 == 1:
            print(2)
        else:
            print(3)
    else:
        print(-1)
