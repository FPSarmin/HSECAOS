m, n, a, b = int(input()), int(input()), int(input()), int(input())
n -= m
if n <= 0:
    print(0)
else:
    more = n % 4
    cost1, cost2 = n * a, 0
    if n % 4 != 0:
        if (n + 3) // 4 * b < more * a + n // 4 * b:
            cost2 = (n + 3) // 4 * b
        else:
            cost2 = more * a + n // 4 * b
    else:
        cost2 = (n + 3) // 4 * b
    if cost1 < cost2:
        print(cost1)
    else:
        print(cost2)
