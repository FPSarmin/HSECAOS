def tree(n, ftree):
    if ftree.get(n, 0) == 0:
        return 0
    return 1 + tree(ftree[n][0], ftree)


n = int(input())
names = set()
myDict = dict()
for i in range(n - 1):
    temp = input().split()
    names |= set([temp[1]]) | set([temp[0]])
    if not temp[0] in myDict:
        myDict[temp[0]] = [temp[1]]
    else:
        myDict[temp[0]].append(temp[1])
for i in sorted(names):
    print(i, tree(i, myDict))
