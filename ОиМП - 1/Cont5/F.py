def IsPointInSquare(x, y):
    return (abs(y)) <= (-abs(x) + 1)


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
