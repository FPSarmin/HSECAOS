n = int(input())
a = []
for i in range(n):
    temp = input().split()
    manData = (int(temp[1]), temp[0])
    a.append(manData)
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i][1])
