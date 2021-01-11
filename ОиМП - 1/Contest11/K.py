from math import sqrt
print(*filter(lambda a: all(map(lambda b: a % b != 0, range(2, int(sqrt(a)) + 1))), range(2, int(input()) + 1)))
