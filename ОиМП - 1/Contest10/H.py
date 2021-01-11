fin = open('input.txt', 'r')
lines = fin.readlines()
names = dict()
for line in lines:
    temp = line.split()
    if not temp[0] in names:
        names[temp[0]] = dict()
    if not temp[1] in names[temp[0]]:
        names[temp[0]][temp[1]] = int(temp[2])
    else:
        names[temp[0]][temp[1]] += int(temp[2])
for i in sorted(names):
    print(i, ':', sep="")
    for j in sorted(names[i]):
        print(j, names[i][j])
