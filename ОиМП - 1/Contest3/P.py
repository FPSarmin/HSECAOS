f0 = 1
f1 = 1
n = int(input())
i = 2
while i < n:
    (f1, f0) = (f0, f1)
    f1 += f0
    i += 1
print(f1)