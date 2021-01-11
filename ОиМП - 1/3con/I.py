import math
a = float(input())
b = float(input())
c = float(input())
d = b * b - 4 * a * c
if d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    if x1 % 1 == 0:
        print(int(x1), end=" ")
    if x2 % 1 == 0:
        print(int(x2))
    if x1 % 1 != 0:
        print("%.7f" % x1, end=" ")
    if x2 % 1 != 0:
        print("%.7f" % x2)
elif d == 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    if x1 % 1 == 0:
        print(int(x1))
    else:
        print("%.7f" % x1)
