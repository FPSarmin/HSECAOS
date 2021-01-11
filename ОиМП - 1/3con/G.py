import math
n = float(input())
i = 1
answer = 0
while i <= n:
    answer += round(10000000 / (i**2))
    i += 1
print(round(answer / 10000000, 5))
