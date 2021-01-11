def IsPointInArea(x, y):
    return ((x + 1) ** 2 + (y - 1) ** 2 <= 4 and
            y >= 2 * x + 2 and y >= -x) or\
           (((x + 1) ** 2 + (y - 1) ** 2 == 4 or
            (x + 1) ** 2 + (y - 1) ** 2 > 4) and
            y <= 2 * x + 2 and y <= -x)


x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print("YES")
else:
    print("NO")
