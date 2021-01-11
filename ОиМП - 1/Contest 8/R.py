maxMarks = [0, 0, 0]
secondWin = [0, 0, 0]
fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
for line in lines:
    name, surname, grade, mark = line.split()
    if secondWin[int(grade) % 3] < int(mark) < maxMarks[int(grade) % 3]:
        secondWin[int(grade) % 3] = int(mark)
    if maxMarks[int(grade) % 3] < int(mark):
        (secondWin[int(grade) % 3], maxMarks[int(grade) % 3])\
            = (maxMarks[int(grade) % 3], int(mark))
print(*secondWin)
