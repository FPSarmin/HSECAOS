def IsAscending(a):
    for i in range(len(a) - 1):
        if a[i + 1] <= a[i]:
            return False
    return True


a = list(map(int, input().split()))
if IsAscending(a):
    print("YES")
else:
    print("NO")
