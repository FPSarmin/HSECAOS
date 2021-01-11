n, k = map(int, input().split())
a = list(("I " * n).split())
for i in range(k):
    temp1, temp2 = map(int, input().split())
    for j in range(temp1 - 1, temp2):
        a[j] = '.'
print("".join(a))