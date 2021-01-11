m = int(input())
n = int(input())
if n >= m:
    max = n
    premax = m
else:
    max = m
    premax = n
while n != 0:
    n = int(input())
    if n >= max:
        (max, premax) = (premax, max)
        max = n
    elif n >= premax:
        premax = n
print(premax)
