a, b, n = map(int, input().split())
spent = (a * 100 + b) * n
print(spent // 100, spent % 100)
