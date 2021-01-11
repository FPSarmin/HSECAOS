def IsPointInSquare(x, y):
    return int(abs((x * x + y * y)**0.5) <= 1)


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("Yes")
else:
    print("NO")
