a = input()
a = a.strip()
while a.find("  ") != -1:
    a = a.replace("  ", " ")
print(a)