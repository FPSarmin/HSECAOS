fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
students = []
for line in lines:
    surname, name, grade, mark = line.split()
    students.append((surname, name, mark))
students.sort()
for i in range(len(students)):
    print(students[i][0], students[i][1], students[i][2])
