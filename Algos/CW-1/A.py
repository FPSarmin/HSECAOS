from sys import stdin


n = int(stdin.readline())
pilot = []
platinum = []
godia = []
regular = []
steward = []
for _ in range(n):
    temp = stdin.readline().split()
    if temp[1] == 'pilot':
        pilot.append(temp[0])
    elif temp[1] == 'platinum':
        platinum.append(temp[0])
    elif temp[1] == 'gold' or temp[1] == 'diamond':
        godia.append(temp[0])
    elif temp[1] == 'regular':
        regular.append(temp[0])
    else:
        steward.append(temp[0])
answer = pilot + platinum + godia + regular + steward
for x in answer:
    print(x)
