x, y = map(int, input().split())
count = 0
while x < y:
    x += 0.7 * x
    count += 1
print(count)
