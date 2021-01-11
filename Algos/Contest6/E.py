from sys import stdin


n = int(stdin.readline())
h = set()
ans = 0
for i in range(n):
    a, b = map(int, stdin.readline().split())
    h.add((a, b, i % 2))
    if (a - 1, b - 1, i % 2) in h:
        if (a - 2, b - 2, i % 2) in h or (a + 1, b + 1, i % 2) in h:
            ans = i + 1
            break
    if (a + 1, b + 1, i % 2) in h:
        if (a + 2, b + 2, i % 2) in h or (a - 1, b - 1, i % 2) in h:
            ans = i + 1
            break
    if (a, b - 1, i % 2) in h:
        if (a, b - 2, i % 2) in h or (a, b + 1, i % 2) in h:
            ans = i + 1
            break
    if (a, b + 1, i % 2) in h:
        if (a, b + 2, i % 2) in h or (a, b - 1, i % 2) in h:
            ans = i + 1
            break
    if (a - 1, b, i % 2) in h:
        if (a - 2, b, i % 2) in h or (a + 1, b, i % 2) in h:
            ans = i + 1
            break
    if (a + 1, b, i % 2) in h:
        if (a + 2, b, i % 2) in h or (a - 1, b, i % 2) in h:
            ans = i + 1
            break
    if (a + 1, b - 1, i % 2) in h:
        if (a + 2, b - 2, i % 2) in h or (a - 1, b + 1, i % 2) in h:
            ans = i + 1
            break
    if (a - 1, b + 1, i % 2) in h:
        if (a - 2, b + 2, i % 2) in h or (a + 1, b - 1, i % 2) in h:
            ans = i + 1
            break
print(ans)
# я более чем уверен,
# что можно было сделать это в 1 ифе или даже код поменьше,
# но так иногда хочется решить в лоб
