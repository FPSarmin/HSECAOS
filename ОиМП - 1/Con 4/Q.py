str = input()
pos1 = str.find("h")
pos2 = str.rfind("h")
print(str[:pos2], str[pos1 + 1:],sep="")
