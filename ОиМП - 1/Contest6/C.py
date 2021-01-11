n = int(input())
max = int('9' * n)
if n == 1:
    min = 0
else:
    min = int('1' + '0' * (n - 1))
for _ in range(max, min, -2):
    print(_, end=" ")
