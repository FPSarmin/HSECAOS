fin = open('input.txt', 'r')
lines = fin.readlines()
words = dict()
wordsCount = dict()
for line in lines:
    for word in line.split():
        words[word] = words.get(word, 0) + 1
for i in sorted(words):
    wordsCount[words[i]] = wordsCount.get(words[i], i)
for i in sorted(wordsCount, reverse=True):
    print(wordsCount[i])
    break
