fin = open('input.txt', 'r')
lines = fin.readlines()
words = dict()
for line in lines:
    for word in line.split():
        words[word] = words.get(word, -1) + 1
        print(words[word], end=" ")
