def rec(n):
    if n == 0:
        return 3
    return 2 * (rec(n - 1) + 1)


n = input()
if n.isdigit():
    print(rec(int(n)))
else:
    print("Incorrect input")
