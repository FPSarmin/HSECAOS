def MinDivisor(n):
    i = 2
    while i * i <= n:
        if n % i == 0 and i != n:
            return i
        i += 1
    return n


n = int(input())
print(MinDivisor(n))
