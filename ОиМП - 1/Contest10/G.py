fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
pres = dict()
sum = 0
for line in lines:
    pres[line.strip()] = pres.get(line.strip(), 0) + 1
    sum += 1
isPrinted = False
for i in sorted(pres, key=lambda x: (-pres[x], x)):
    print(i)
    if pres[i] / sum <= 0.5 and not isPrinted:
        isPrinted = True
    elif isPrinted or pres[i] / sum > 0.5:
        break
