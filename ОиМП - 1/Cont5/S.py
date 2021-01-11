def rec():
    n = int(input())
    if n != 0:
        return n + rec()
    if n == 0:
        return 0


print(rec())