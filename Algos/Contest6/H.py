from sys import stdin


myStr = stdin.readline()
pows = [0 for _ in range(len(myStr))]
pows[0] = 1
for i in range(1, len(myStr)):
    pows[i] = pows[i-1] * 31
h = [0 for _ in range(len(myStr))]
h[0] = (ord(myStr[0]) - ord('a') + 1) * pows[0]
for i in range(1, len(myStr)):
    h[i] = (ord(myStr[i]) - ord('a') + 1) * pows[i]
    h[i] += h[i - 1]
n = int(stdin.readline())
for i in range(n):
    l, a, b = map(int, stdin.readline().split())
    tmp = h[a + l]
    if a:
        tmp -= h[a - 1]
    tmp1 = h[b + l]
    if b:
        tmp1 -= h[b - 1]
    if a < b:
        tmp *= pows[b - a]
    if b < a:
        tmp1 *= pows[a - b]
    if tmp - tmp1 < 0:
        print(-1)
    if tmp == tmp1:
        print(0)
    if tmp - tmp1 > 0:
        print(1)
