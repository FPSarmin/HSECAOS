a = int(input())
b = int(input())
if a % (b - a + 1) == 1 and b % (b - a + 1) == 0 or a == b:
    print("YES")
else:
    print("NO")
