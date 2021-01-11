from sys import stdin


def check(a, m, d):
    stalls = 1
    last_stall = a[0] - m
    for i in range(1, len(a)):
        if a[i] - last_stall >= d:
            last_stall = last_stall + d if last_stall + d > a[i] - m\
                else a[i] - m
            stalls += 1
        elif a[i] + m >= last_stall + d:
            last_stall += d
            stalls += 1
    return stalls < len(a)


def binSearch(a, d):
    L = 0
    R = 10**10
    epsilon = 10**(-7)
    while R - L > epsilon:
        m = (R + L) / 2
        if check(a, m, d):
            L = m
        else:
            R = m
    return L


n, d = map(int, stdin.readline().split())
x = sorted(list(map(int, stdin.readline().split())))
print(f"{binSearch(x, d):.{6}f}")
