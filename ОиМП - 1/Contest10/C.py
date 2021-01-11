n = int(input())
synonyms = dict()
for i in range(n):
    temp1, temp2 = input().split()
    synonyms[temp1] = temp2
    synonyms[temp2] = temp1
print(synonyms[input()])
