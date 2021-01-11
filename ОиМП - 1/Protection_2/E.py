def sumik(i, k, a):
    sum = 0
    for j in range(i, i + k):
        sum += a[j]
    return sum


n = int(input())
answer = []
for i in range(n):
    temp = list(input().split())
    if temp[0] == 'push':
        answer.append(int(temp[1]))
    elif temp[0] == 'pop':
        answer.pop()
    elif temp[0] == 'print':
        print(*answer)
    elif temp[0] == 'sum':
        answer.append(sumik(int(temp[1]), int(temp[2]), answer))
