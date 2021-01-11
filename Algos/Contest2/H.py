from sys import stdin


expo = []
n, m = map(int, stdin.readline().split())
for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    for j in range(m):
        expo.append((temp[j], i, j))
cams = list(map(int, stdin.readline().split()))
expo.sort()
cams.sort()
answer = [[0 for _ in range(m)] for j in range(n)]
for i in range(n * m):
    answer[expo[i][1]][expo[i][2]] = cams[i]
for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()
