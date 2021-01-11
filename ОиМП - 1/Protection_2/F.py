def tree(n):
    if n == 0:
        return 1
    return tree(n // 3) + tree(n // 2)


n = int(input())
print(tree(n))
