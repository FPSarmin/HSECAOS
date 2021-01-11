fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
names = True
parties = []
votes = []
for line in lines:
    if not names:
        temp = parties.index(line.strip())
        votes[temp][1] += 1
        continue
    if names and line.strip() != "PARTIES:" and line.strip() != "VOTES:":
        parties.append(line.strip())
        votes.append([line.strip(), 0])
    if line.strip() == "VOTES:":
        names = False
votes.sort(key=lambda x: (-x[1], x[0]))
for i in range(len(votes)):
    print(votes[i][0])
