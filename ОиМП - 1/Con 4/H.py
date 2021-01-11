import math
n = int(input())
x = float(input())
a = float(input())
answer = a
while n != 0:
    a = float(input())
    answer = round(answer * x + a, 12)
    n -= 1
if answer % 1 != 0:
    print(round(answer, 2))
else:
    print(int(answer))
