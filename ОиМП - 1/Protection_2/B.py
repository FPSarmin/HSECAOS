q = int(input())
a = list(map(int, input().split()))
isSolved = False
for i in range(100):
    if a[0] + a[1] * i + a[2] * i**2 + a[3] * i**3 + a[4] * i**4 + a[5] * i**5 == q:
        isSolved = True
        print(i)
        break
if not isSolved:
    print(-1)
