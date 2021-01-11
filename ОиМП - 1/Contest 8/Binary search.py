def binary_search(numbers, x, left=0, right=0):
    if len(numbers) == 0:
        return -1
    if right - 1 == left and numbers[(right + left) // 2] != x:
        return -1
    if numbers[(right + left) // 2] == x:
        return right - 1
    else:
        if numbers[(right + left) // 2] > x:
            return binary_search(numbers, x, left=left, right=(right + left) // 2)
        if numbers[(right + left) // 2] < x:
            return binary_search(numbers, x, left=(right + left) // 2, right=right)


a = list(map(int, input().split()))
x = int(input())
print(binary_search(a, x, right=len(a)))
