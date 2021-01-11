posled = []
mySet = set()
line = int(input())
while line != -2000000000:
    posled.append(line)
    mySet.add(line)
    line = int(input())
sortPos = sorted(posled)
revSortPos = sorted(posled, reverse=True)
if sortPos[0] == sortPos[len(sortPos) - 1]:
    print('CONSTANT ')
elif posled == sortPos:
    if len(mySet) == len(posled):
        print('ASCENDING')
    else:
        print('WEAKLY ASCENDING')
elif posled == revSortPos:
    if len(mySet) == len(posled):
        print('DESCENDING ')
    else:
        print('WEAKLY DESCENDING')
else:
    print('RANDOM ')
