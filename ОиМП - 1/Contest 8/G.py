n = int(input())
a = list(map(int, input().split()))
k = int(input())
p = list(map(int, (input().split())))
for j in range(k):
    a[p[j] - 1] -= 1
for i in range(len(a)):
    if a[i] < 0:
        print("YES")
    else:
        print("NO")

