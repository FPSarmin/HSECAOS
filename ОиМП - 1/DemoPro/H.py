a = input()
pos1 = a.find('h')
pos2 = a.rfind('h')
print(a[:pos1], a[pos2:pos1:-1], a[pos2:], sep="")
