def maxNums(a):
    num1 = a[-1] * a[-2] * a[-3]
    num2 = a[0] * a[1] * a[2]
    num3 = a[-1] * a[-2] * a[0]
    if num1 >= num2 and num1 >= num2:
        return a[-1], a[-2], a[-3]
    if num2 >= num1 and num2 >= num3:
        return a[0], a[1], a[2]
    if num3 >= num1 and num3 >= num2:
        return a[-1], a[-2], a[0]


a = list(map(int, input().split()))
a.sort(reverse=True)
print(*maxNums(a))
