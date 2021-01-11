def move(n, x, y):
    if n > 0:
        move(n - 1, x, 6 - x - y)
        print(n, x, y)
        move(n - 1, 6 - x - y, y)


def move2(n, x, y):
    if n > 0:
        move(n - 1, x, 6 - x - y)
        print(n, x, y)
        if n > 3:
            move(n - 3, 6 - x - y, x)
            print(n - 2, 6 - x - y, y)
            move2(n - 3, x, 6 - x - y)
        elif n == 3:
            print(n - 2, 6 - x - y, y)


n = int(input())
move2(n, 1, 3 - n % 2)
