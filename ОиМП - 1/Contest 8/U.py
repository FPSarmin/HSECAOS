fin = open('input.txt', 'r', encoding='utf8')
lines = fin.readlines()
names = True
parties = []
votes = []
votesCount = 0
for line in lines:
    if not names:
        votes[parties.index(line.strip())] += 1
        votesCount += 1
        continue
    if names and line.strip() != "PARTIES:" and line.strip() != "VOTES:":
        parties.append(line.strip())
        votes.append(0)
    if line.strip() == "VOTES:":
        names = False
for i in range(len(votes)):
    if votes[i] / votesCount >= 0.07:
        print(parties[i])
