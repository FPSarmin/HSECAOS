a = int(input())
b = int(input())
c = int(input())
if c == 0:
    x = -b / a
    if x < -b / a or x % 1 != 0:
        print("NO SOLUTION")
    else:
        print(int(x))
if (a == 0 and c**2 - b != 0) or c < 0:
    print("NO SOLUTION")
elif a == 0 and c**2 - b == 0:
    print("MANY SOLUTIONS")
else:
    x = (c**2 - b) / a
    if x < -b / a or x % 1 != 0:
        print("NO SOLUTION")
    else:
        print(int(x))
