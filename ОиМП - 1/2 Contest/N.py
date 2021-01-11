a = int(input())
b = int(input())
c = int(input())
count = (a == b) * 1 + (a == c) * 1 + (b == c) * 1
if count == 0:
    print(0)
elif count == 1:
    print(count + 1)
else:
    print(count)
