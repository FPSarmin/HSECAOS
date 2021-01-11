from sys import stdin


def addH(num):
    if not find(num):
        h[num % n].append(num)
    return len(h[num % n])


def find(num):
    for i in range(len(h[num % n])):
        if h[num % n][i] == num:
            return 1
    return 0


def remove(num):
    for i in range(len(h[num % n])):
        if h[num % n][i] == num:
            h[num % n][i], h[num % n][-1] = h[num % n][-1], h[num % n][i]
            h[num % n].pop()
            return 1
    return 0


n, q = map(int, stdin.readline().split())
h = [[] for _ in range(n)]
for i in range(q):
    command = stdin.readline().split()
    if command[0] == 'add':
        print(addH(int(command[1])))
    elif command[0] == 'find':
        print(find(int(command[1])))
    elif command[0] == 'remove':
        print(remove(int(command[1])))
