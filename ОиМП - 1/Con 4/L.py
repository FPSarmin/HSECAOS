str = input()
pos = 0
count = 0
while pos != -1:
    pos = str.find(" ", pos + 1)
    count += 1
if count == 0:
    print(1)
else:
    print(count)
