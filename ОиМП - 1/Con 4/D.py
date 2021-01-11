import math
p = float(input())
x = float(input())
y = float(input())
amount = x * 100 + y + math.floor((x * 100 + y) * p / 100)
print(math.floor(amount / 100), int(round(amount / 100 % 1, 2) * 100))
