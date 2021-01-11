n, m, k = map(int, input().split())
pole = [[0 for i in range(m)] for j in range(n)]
for i in range(k):
    x, y = map(lambda a: int(a) - 1, input().split())
    pole[x][y] = '*'
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) == (0, 0):
                continue
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if pole[x + dx][y + dy] != '*':
                    pole[x + dx][y + dy] += 1
for i in range(n):
    for j in range(m):
        print(pole[i][j], end=' ')
    print()
