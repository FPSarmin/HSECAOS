def countaoe(a: str):
    count = 0
    count += a.count('a')
    count += a.count('i')
    count += a.count('e')
    count += a.count('o')
    count += a.count('u')
    return count


n = int(input())
spells = []
for i in range(n):
    temp = input()
    spells.append((temp, countaoe(temp)))
spells.sort(key=lambda x: (-x[1], len(x[0])))
for i in range(len(spells)):
    print(spells[i][0])
