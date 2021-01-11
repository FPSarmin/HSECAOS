a = input()
pos = a.find(" ")
max = pos
pos1 = 0
answer = a[0:pos]
while pos != -1:
    pos1 = pos
    pos = a.find(" ", pos + 1)
    if pos - pos1 > max and pos != -1:
        answer = a[pos1 + 1:pos]
if len(a) + 1 - a.rfind(" ") >= max:
    print(a[a.rfind(" ") + 1:len(a) + 1])
else:
    print(answer)