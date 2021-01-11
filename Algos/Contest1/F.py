from sys import stdin

n = int(stdin.readline())
lombardItems = [(0, 0)]
head = 1
sum = 0
for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    if temp[0] == 1:
        lombardItems.append((temp[1], lombardItems[-1][1] if temp[1] < lombardItems[lombardItems[-1][1]][0] else head))
        sum += temp[1]
        head += 1
    elif head == 1:
        print(0)
    elif temp[0] == 2:
        head -= 1
        sum -= lombardItems.pop()[0]
    elif temp[0] == 3:
        print(sum)
    elif temp[0] == 4:
        print(lombardItems[lombardItems[-1][1]][0])
    elif temp[0] == 5:
        print(head - lombardItems[-1][1])
