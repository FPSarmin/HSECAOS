a = list(map(int, input().split()))
height = int(input())
placed = False
if a[0] < height:
    print(1)
else:
    for i in range(len(a) - 1):
        if a[i] >= height > a[i + 1]:
            print(i + 2)
            placed = True
            break
    if not placed:
        print((len(a) + 1))
