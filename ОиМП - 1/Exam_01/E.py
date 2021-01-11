n = int(input())
numbers = {816, 817, 395}
tariff = {1: 0, 2: 0, 3: 0}
mySet = {i for i in range(1, 32)}
days = [60 for i in range(31)]
for i in range(n):
    number, day, callB, callE = input().split()
    callB = list(map(int, callB.split(":")))
    callE = list(map(int, callE.split(":")))
    time = (callE[0] * 3600 + callE[1] * 60 + callE[0]) - (callB[0] * 3600 + callB[1] * 60 + callB[0])
    tariff[1] += 240
    tariff[1] += 2 * (time - 60) if time > 60 else 0
    if days[int(day) - 1] > 0:
        if int(number[:3]) in numbers:
            days[int(day) - 1] -= (time + 59) // 60
            if days[int(day) - 1] < 0:
                if number[:3] == '816':
                    tariff[2] += abs(days[int(day) - 1]) * 150
                elif number[:3] == '817':
                    tariff[2] += abs(days[int(day)] - 1) * 500
                else:
                    tariff[2] += abs(days[int(day)] - 1) * 300
        else:
            tariff[2] += abs(days[int(day) - 1]) * 300
    else:
         if number[:3] == '816':
             tariff[2] += (time + 59) // 60 * 150
         elif number[:3] == '817':
             tariff[2] += (time + 59) // 60 * 500
         else:
             tariff[2] += (time + 59) // 60 * 300
    tariff3 = 110
    tariff3 += ((time + 59) // 60 - 1) * 10 if time > 60 else 0
    tariff[3] += max(2000, tariff3)
    if int(day) in mySet:
        mySet.remove(int(day))
tariff[3] += 20 * len(mySet)
for i in tariff:
    print(tariff[i] // 100, tariff[i] % 100, sep='\t')
