fin = open('input.txt', 'r')
lines = fin.readlines()
bank = dict()
for line in lines:
    temp = line.split()
    if temp[0] == 'DEPOSIT':
        bank[temp[1]] = bank.get(temp[1], 0) + int(temp[2])
    elif temp[0] == 'WITHDRAW':
        bank[temp[1]] = bank.get(temp[1], 0) - int(temp[2])
    elif temp[0] == 'TRANSFER':
        bank[temp[1]] = bank.get(temp[1], 0) - int(temp[3])
        bank[temp[2]] = bank.get(temp[2], 0) + int(temp[3])
    elif temp[0] == 'BALANCE':
        print(bank.get(temp[1], 'ERROR'))
    elif temp[0] == 'INCOME':
        for i in bank:
            if bank[i] <= 0:
                continue
            bank[i] = int(bank[i] * (1 + int(temp[1]) / 100))
