def countUpper(word):
    count = 0
    for i in range(len(word)):
        if word[i].isupper():
            count += 1
    return count


n = int(input())
myDict = dict(list())
for i in range(n):
    temp = input()
    word = temp.lower()
    if word in myDict:
        myDict[word].append(temp)
    else:
        myDict[word] = [temp]
count = 0
string = input().split()
for word in string:
    temp = word.lower()
    if (temp in myDict and word not in myDict[temp]) \
            or (countUpper(word) != 1):
        count += 1
print(count)
