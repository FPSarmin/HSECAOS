fin = open('input.txt', 'r')
lines = fin.readlines()
a = set()
for line in lines:
    a |= set(line.split())
print(len(a))
