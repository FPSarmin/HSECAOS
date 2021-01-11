a = list(input().split())
k = int(input())
a = a[k::-1] + a[:k:-1]
a.reverse()
a.pop()
a = a[len(a) - k - 1::-1] + a[:len(a) - k - 1:-1]
a.reverse()
print(*a)
