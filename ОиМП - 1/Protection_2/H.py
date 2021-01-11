n = int(input())
cords = []
isPer = False
for i in range(n):
    cords.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i != j and (cords[i][0] < cords[j][0] and cords[i][1] < cords[j][1]) or\
                (cords[i][0] > cords[j][0] and cords[i][1] > cords[j][1]):
            continue
        elif i != j:
            print("YES")
            isPer = True
            break
    if isPer:
        break
if not isPer:
    print("NO")
