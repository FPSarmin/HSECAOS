from copy import deepcopy


def neighbors_count(a, x, y):
    ans = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) == (0, 0):
                continue
            if 0 <= x + dx < len(a) and 0 <= y + dy < len(a):
                ans += a[x + dx][y + dy]
    return ans


def transform(a, delta_time):
    ans = deepcopy(a)

    for _ in range(delta_time):
        a = deepcopy(ans)

        for i in range(len(a)):
            for j in range(len(a)):

                k = neighbors_count(a, i, j)

                if k < 2 or k > 3:
                    ans[i][j] = 0
                if not a[i][j] and k == 3:
                    ans[i][j] = 1

    return ans


n, T = map(int, input().split())

field = [
    [int(x) for x in input().split()]
    for _ in range(n)
]

for line in transform(field, T):
    print(*line)
