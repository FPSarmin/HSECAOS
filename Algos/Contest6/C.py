from sys import stdin


def addH(num):
    tmp = num % n
    while h[tmp % n] is not None and\
            h[tmp % n] != num and h[tmp % n] != -1:
        tmp += 1
    h[tmp % n] = num
    return tmp % n


def findH(num):
    tmp = num % n
    count = 0
    while count != n:
        if h[tmp % n] == num:
            return 1
        tmp += 1
        count += 1
    return 0


def removeH(num):
    tmp = num % n
    count = 0
    while count != n:
        if h[tmp % n] == num:
            h[tmp % n] = -1
            return 1
        count += 1
        tmp += 1
    return 0


n, q = map(int, stdin.readline().split())
h = [None for _ in range(n)]
for i in range(q):
    command = stdin.readline().split()
    if command[0] == 'add':
        print(addH(int(command[1])))
    elif command[0] == 'find':
        print(findH(int(command[1])))
    elif command[0] == 'remove':
        print(removeH(int(command[1])))
