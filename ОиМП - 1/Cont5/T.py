def rec():
    n = int(input())
    global ishave
    if n == 0:
        return
    if n**0.5 % 1 == 0:
        ishave += 1
        rec()
        print(n, end=" ")
    else:
        rec()


ishave = 0
rec()
if not ishave:
    print(0)
