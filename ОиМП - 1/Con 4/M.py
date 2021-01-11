str = input()
pos = str.find(" ")
print(str[pos + 1:], end=" ")
print(str[:pos + 1])
