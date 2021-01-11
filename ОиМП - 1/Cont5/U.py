def move(a, b, c, n):
    if n == 1:
        print (a, a, c)
        return
    else:
        move(a, c, b, n - 1)
        print(a, a,)