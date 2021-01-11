sumMarks = [0, 0, 0]
countMarks = [0, 0, 0]
fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
for line in lines:
    name, surname, grade, mark = line.split()
    sumMarks[int(grade) % 3] += int(mark)
    countMarks[int(grade) % 3] += 1
print(sumMarks[0] / countMarks[0],
      sumMarks[1] / countMarks[1],
      sumMarks[2] / countMarks[2])
