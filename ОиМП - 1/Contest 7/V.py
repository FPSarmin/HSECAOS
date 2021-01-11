x = []
y = []
for i in range(8):
    temp = list(map(int, input().split()))
    x.append(temp[0])
    y.append(temp[1])
isPos = True
for i in range(8):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j]\
                or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            isPos = False
            break
if isPos:
    print("NO")
else:
    print("YES")
