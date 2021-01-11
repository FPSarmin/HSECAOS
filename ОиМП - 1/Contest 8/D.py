a = list(map(int, input().split()))
a.sort(reverse=True)
if a[-1] * a[-2] > a[0] * a[1]:
    print(a[-1], a[-2])
else:
    print(a[1], a[0])
