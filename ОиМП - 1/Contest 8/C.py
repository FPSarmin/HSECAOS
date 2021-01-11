def shDist(a):
    global num
    return abs(a - num)


uselessnum = int(input())
a = list(map(int, input().split()))
num = int(input())
a.sort(key=shDist)
print(a[0])
