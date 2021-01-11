k = int(input())
m = int(input())
n = int(input())
if n > k:
    if 2 * n % k != 0:
        print((n * 2 // k) * m + m)
    else:
        print((n * 2 // k) * m)
else:
    print(2 * m)
