a = int(input())
b = int(input())
c = int(input())
if b < a or c < a:
    if c < a:
        (a, c) = (c, a)
    if b < a:
        (a, b) = (b, a)
if c < b:
    (b, c) = (c, b)
if a + b > c:
    if c**2 < b**2 + a**2:
        print("acute")
    elif c**2 == b**2 + a**2:
        print("rectangular")
    else:
        print("obtuse")
else:
    print("impossible")