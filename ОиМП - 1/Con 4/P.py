str = input()
pos1 = str.find("f")
pos2 = str.find("f", pos1 + 1)
if pos1 == -1:
    print(-2)
elif pos2 == -1:
    print(-1)
else:
    print(pos2)
