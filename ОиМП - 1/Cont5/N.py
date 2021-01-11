def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return i
    if n % 2 == 0:
        a = power(a, abs(n // 2))
        return a * a
    if n % 2 != 0:
        return i * power(a * i, abs(n) - 1)


a = float(input())
n = int(input())
i = a
if n < 0:
    a = 1 / a
    i = a
print(power(a, n))
