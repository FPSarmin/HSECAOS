n = int(input())
ind = True
if n % 2 != 0 and n != 1:
    ind = False
while n % 2 == 0:
    n //= 2
    if n % 2 != 0 and n != 1:
        ind = False
if ind:
    print("YES")
else:
    print("NO")
