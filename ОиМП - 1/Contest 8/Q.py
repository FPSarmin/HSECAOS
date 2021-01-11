maxMarks = [0, 0, 0]
countWin = [0, 0, 0]
fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
for line in lines:
    name, surname, grade, mark = line.split()
    if maxMarks[int(grade) % 3] == int(mark) or countWin[int(grade) % 3] == 0:
        countWin[int(grade) % 3] += 1
        maxMarks[int(grade) % 3] = int(mark)
    elif maxMarks[int(grade) % 3] < int(mark):
        maxMarks[int(grade) % 3] = max(maxMarks[int(grade) % 3], int(mark))
        countWin[int(grade) % 3] = 1
print(*countWin)
