a, b, c, d = map(int, input().split())
bus1 = set(range(min(a, b), max(a, b) + 1))
bus2 = set(range(min(c, d), max(c, d) + 1))
print(len(bus1 & bus2))
