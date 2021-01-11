import math
a = float(input())
b = float(input())
c = float(input())
d = b * b - 4 * a * c
if a != 0 and b != 0 and c != 0:
    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(2, end=" ")
        print(min("%.7f" % x1, "%.7f" % x2), max("%.7f" % x1, "%.7f" % x2))
    elif d == 0:
        x1 = -b / (2 * a)
        print(1, end=" ")
        print("%.7f" % x1)
    else:
        print(0)
elif a != 0 and b != 0 and c == 0:
    x1 = -b / a
    print(2, end=" ")
    print(min("%.7f" % x1, "%.7f" % 0), max("%.7f" % x1, "%.7f" % 0))
elif a == 0 and b != 0 and c != 0:
    print(1, "%.7f" % (-c / b))
elif a == 0 and b == 0 and c == 0:
    print(3)
elif a != 0 and b == 0 and c != 0:
    if c > 0:
        print(0)
    else:
        print(1, end=" ")
        print("%.7f" % (-c / a)**0.5)
elif a == 0 and b == 0 and c != 0:
    print(0)
else:
    print(3)
