def phib(n):
    if n == 1:
        return 'a'
    if n == 2:
        return 'b'
    return phib(n - 2) + phib(n - 1)


n = int(input())
print(phib(n))
