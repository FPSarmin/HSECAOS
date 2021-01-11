n = int(input())
f1 = 1
if n == 1:
    print(1)
f2 = 1
if n == 2:
    print(2)
fn = 0
while n != 1:
    f2 += f1
    f1 = f2 - f1
    n -= 1
print(f2)