from copy import deepcopy


def neighbors_count(A, x, y):
    ans = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) == (0, 0):
                continue
            if 0 <= x + dx < len(A) and 0 <= y + dy < len(A):
                ans += A[x + dx][y + dy]
    return ans


def transform(A, delta_time):
    ans = deepcopy(A)

    for _ in range(delta_time):
        A = deepcopy(ans)

        for i in range(len(A)):
            for j in range(len(A)):

                k = neighbors_count(A, i, j)

                if k < 2 or k > 3:
                    ans[i][j] = 0
                if not A[i][j] and k == 3:
                    ans[i][j] = 1

    return ans


n, T = map(int, input().split())

field = [
    [int(x) for x in input().split()]
    for _ in range(n)
]

for line in transform(field, T):
    print(*line)
