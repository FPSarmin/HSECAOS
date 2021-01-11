import math
n = float(input())
if round((n % 1), 10) >= 0.5:
    print(math.ceil(n))
else:
    print(math.floor(n))