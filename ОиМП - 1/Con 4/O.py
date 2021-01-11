str = input()
pos1 = str.find("h")
pos2 = str.rfind("h")
print(str[:pos1], str[pos2 + 1:], sep="")
