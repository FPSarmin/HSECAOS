import math
p = float(input())
x = float(input())
y = float(input())
k = float(input())
amount = x * 100 + y
i = 0
while i < k:
    amount += math.floor(amount * p / 100)
    i += 1
print(math.floor(amount / 100), int(round(amount / 100 % 1, 2) * 100))
