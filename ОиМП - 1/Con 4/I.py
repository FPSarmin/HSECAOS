import math
a = float(input())
b = float(input())
c = float(input())
d = b * b - 4 * a * c
if d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print(min("%.7f" % x1, "%.7f" % x2), max("%.7f" % x1, "%.7f" % x2))
elif d == 0:
    x1 = -b / (2 * a)
    print("%.7f" % x1)
