n, m = map(int, input().split())
aZero, x, y = map(int, input().split())
sIn = [(aZero, aZero)]
sOut = []
for i in range(1, m):
    item = (sIn[-1][0] * x + y) % 1000000007
    sIn.append((item, min(item, sIn[-1][1])))
sum = sIn[-1][1]
for i in range(m, n):
    item = (sIn[-1][0] * x + y) % 1000000007 if len(sIn) != 0 else (sOut[0][0] * x + y) % 1000000007
    sIn.append((item, item if len(sIn) == 0 else min(sIn[-1][1], item)))
    if len(sOut) == 0:
        while len(sIn) != 0:
            item = sIn.pop()[0]
            sOut.append((item, item if len(sOut) == 0 else min(item, sOut[-1][1])))
    item = sOut.pop()
    if len(sIn) == 0 or len(sOut) == 0:
        sum += sOut[-1][1] if len(sIn) == 0 else sIn[-1][1]
    else:
        sum += min(sIn[-1][1], sOut[-1][1])
print(sum)
