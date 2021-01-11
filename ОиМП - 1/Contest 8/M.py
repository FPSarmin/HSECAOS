def merge(a, b):
    i = 0
    j = 0
    c = [0] * (len(a) + len(b))
    while i + j < len(a) + len(b):
        if a[i] <= b[j]:
            c[i + j] = a[i]
            i += 1
        if i == len(a):
            while j < len(b):
                c[i + j] = b[j]
                j += 1
        elif b[j] <= a[i]:
            c[i + j] = b[j]
            j += 1
        if j == len(b):
            while i < len(a):
                c[i + j] = a[i]
                i += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
