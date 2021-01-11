n = int(input())
gameList = list(map(int, input().split())) + [0]
gameStack = []
count = 0
for i in range(n):
    if len(gameStack) == 0 or gameStack[-1][0] != gameList[i]:
        gameStack.append((gameList[i], 1))
    else:
        gameStack.append((gameList[i], gameStack[-1][1] + 1))
        if gameStack[-1][1] >= 3 and gameList[i + 1] != gameList[i]:
            temp = gameStack[-1][0]
            count += gameStack[-1][1]
            while len(gameStack) != 0 and gameStack[-1][0] == temp:
                gameStack.pop()
print(count)
