n = int(input())
myDict = dict()
for i in range(n):
    temp = input().split()
    for j in range(1, len(temp)):
        myDict[temp[j]] = temp[0]
m = int(input())
for i in range(m):
    print(myDict[input().strip()])
