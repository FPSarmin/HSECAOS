from sys import stdin


n = int(stdin.readline())
price = []
pos = []
neg = []
for i in range(n):
    temp = stdin.readline().split()
    price.append((float(temp[0]), i))
    pos.append((int(temp[1]), i))
    neg.append((int(temp[2]), i))
price.sort(key=lambda x: x[0])
pos.sort(key=lambda x: -x[0])
neg.sort(key=lambda x: x[0])
bestPrice = set()
bestPos = set()
bestNeg = set()
for i in range((n + 1) // 2):
    bestPrice.add(price[i][1])
    bestPos.add(pos[i][1])
    bestNeg.add(neg[i][1])
print(len(bestPrice & bestNeg & bestPos))
