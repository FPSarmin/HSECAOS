n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m):
    temp1, temp2 = map(int, input().split())
    minimum = a.index(min(a[temp1:temp2 + 1]))
    mini = a[minimum]
    notmini = mini
    for i in range(temp1, temp2 + 1):
        if a[i] != mini:
            notmini = a[i]
            break

    print(notmini) if mini != notmini else print('NOT FOUND')
