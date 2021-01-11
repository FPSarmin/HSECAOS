x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y1 % 2 == y2 % 2:
    if x1 % 2 == x2 % 2:
        print("YES")
    else:
        print("NO")
else:
    if x1 % 2 != x2 % 2:
        print("YES")
    else:
        print("NO")
