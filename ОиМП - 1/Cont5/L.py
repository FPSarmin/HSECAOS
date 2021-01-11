global i


def power(a, n):
    i = a
    if n == 0:
        return 1
    if n < 0:
        a = 1 / a
        i = a
        n = abs(n)
    while True:
        if n <= 1:
            return a
        a *= i
        n -= 1


a = float(input())
n = float(input())
print(power(a, n))
