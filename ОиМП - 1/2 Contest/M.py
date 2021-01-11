a = int(input())
b = int(input())
c = int(input())
if b < a or c < a:
    if c < a:
        (a, c) = (c, a)
    if b < a:
        (a, b) = (b, a)
if c < b:
    (b, c) = (c, b)
print(a, b, c)
