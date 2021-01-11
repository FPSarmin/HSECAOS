def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)


def ReduceFraction(n, m):
    gcd_num = gcd(n, m)
    while gcd_num != 1:
        n //= gcd_num
        m //= gcd_num
        gcd_num = gcd(n, m)
    print(n, m)


n = int(input())
m = int(input())
ReduceFraction(n, m)
