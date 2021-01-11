a = list(input().split())
b = [a[-1]]
b.extend(a[:len(a) - 1])
print(*b)