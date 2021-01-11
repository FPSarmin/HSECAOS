fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
schools = [(0, 0)] * 100
for line in lines:
    schNum = int(line.split()[2])
    schools[schNum] = (schools[schNum][0] + 1, schNum)
schools.sort(reverse=True, key=lambda x: (x[0], -x[1]))
for i in range(len(schools) - 1):
    if schools[0][0] != schools[i][0]:
        break
    print(schools[i][1], end=" ")
