def IsPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0 and i != n:
            return False
        i += 1
    return True


n = int(input())
if IsPrime(n):
    print("YES")
else:
    print("NO")
