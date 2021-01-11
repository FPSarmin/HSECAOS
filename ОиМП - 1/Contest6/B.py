a, b = int(input()), int(input())
c = 1
if a >= b:
    c = -1
for _ in range(a, b + c, c):
    print(_, end=" ")
