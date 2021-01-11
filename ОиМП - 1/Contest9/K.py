n, k = map(int, input().split())
a, b = map(int, input().split())
holidays = set(range(7, n + 1, 7))
holidays |= set(range(6, n + 1, 7))
answer1 = set(range(a, n + 1, b))
for i in range(1, k):
    a, b = map(int, input().split())
    firstDay = set(range(a, n + 1, b))
    answer1 |= firstDay
answer1 -= holidays
print(len(answer1))
