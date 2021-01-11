import math
n = float(input()) * 100
print(math.floor(n / 100), int(round(n / 100 % 1, 2) * 100))