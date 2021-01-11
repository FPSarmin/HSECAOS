a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a != 0:
    y = (a * f - c * e) / (a * d - c * b)
    x = (e - b * y) / a
elif b != 0:
    x = (f * b - d * e) / (b * c - a * d)
    y = (e - a * x) / b
print("%.7f" % x, "%.7f" % y)
