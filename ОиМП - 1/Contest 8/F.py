def CountSort(a):
    c = [0] * 101
    for i in range(len(a)):
        c[a[i]] += 1
    for i in range(len(c)):
        while c[i] >= 1:
            print(i, end=" ")
            c[i] -= 1


a = list(map(int, input().split()))
CountSort(a)
