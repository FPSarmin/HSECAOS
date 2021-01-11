str = input()
pos1 = str.find("f")
pos2 = str.rfind("f")
if -1 != pos1 == pos2 != -1:
    print(pos1)
elif -1 != pos1 != pos2 != -1:
    print(pos1, pos2)
