def bitsCount(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return num % 2 + bitsCount(num // 2)


n = input()
listOfNums = list(map(int, input().split()))
print(*sorted(listOfNums))
print(*sorted(listOfNums, key=lambda x: (-bitsCount(x), x)))
