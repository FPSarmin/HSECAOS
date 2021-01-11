from math import floor
fin = open('input.txt', 'r')
lines = fin.readlines()
parties = list()
votes = dict()
sum = 0
for line in lines:
    temp = line.split()
    parties.append(' '.join(temp[:-1]))
    votes[' '.join(temp[:-1])] = int(temp[-1])
    sum += int(temp[-1])
currplaces = 450
votingNum = sum / 450
answer = dict(votes)
for i in answer:
    answer[i] /= votingNum
    answer[i] = floor(answer[i])
    currplaces -= answer[i]
while currplaces > 0:
    for i in sorted(answer, key=lambda x: (
            -(votes[x] / votingNum % 1), votes[x])
                    ):
        answer[i] += 1
        currplaces -= 1
        if currplaces == 0:
            break
for i in parties:
    print(i, answer[i])
