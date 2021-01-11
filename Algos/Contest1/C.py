def insSort(nums, k):
    for i in range(1, len(nums)):
        j = 0
        while nums[i - j] < nums[i - j - 1] and j < i:
            (nums[i - j], nums[i - j - 1]) = (nums[i - j - 1], nums[i - j])
            j += 1
        if i == k:
            return nums


n = int(input())
listOfNums = list(map(int, input().split()))
k = int(input())
print(*insSort(listOfNums, k))
