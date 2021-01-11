n = int(input())
answer1 = set({})
answer2 = set({})
for i in range(n):
    temp = int(input())
    tempSet = set({})
    for j in range(temp):
        tempSet |= set({input()})
    if answer1 == set({}) and i == 0:
        answer1 |= tempSet
    else:
        answer1 &= tempSet
    answer2 |= tempSet
print(len(answer1))
print(*sorted(answer1, reverse=True), sep="\n")
print(len(answer2))
print(*sorted(answer2, reverse=True), sep="\n")
