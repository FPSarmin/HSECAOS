a = input().strip()
a = a.replace('.', ' ')
a = a.replace('!', ' ')
a = a.replace('?', ' ')
a = a.replace(' - ', ' ')
a = a.replace(',', ' ')
while a.find("  ") != -1:
    a = a.replace('  ', ' ')
count = 0
pos = 0
a = a.strip()
while pos != -1:
    pos = a.find(" ", pos + 1)
    count += 1
print(count)
