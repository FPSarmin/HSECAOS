def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return power(a * i, n - 1)


a = float(input())
i = a
n = int(input())
print(power(a, n))
