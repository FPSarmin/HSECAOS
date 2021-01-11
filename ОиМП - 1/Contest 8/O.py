maxMarks = [0, 0, 0]
fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
for line in lines:
    name, surname, grade, mark = line.split()
    maxMarks[int(grade) % 3] = max(maxMarks[int(grade) % 3], int(mark))
print(*maxMarks)
