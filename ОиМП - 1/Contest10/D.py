fin = open('input.txt', 'r')
lines = fin.readlines()
myDict = dict()
for line in lines:
    temp = line.split()
    myDict[temp[0]] = myDict.get(temp[0], 0) + int(temp[1])
for i in sorted(myDict):
    print(i, myDict[i])
