def merge(numsA, numsB):
    result = []
    while len(numsA) != 0 and len(numsB) != 0:
        if numsA[0] < numsB[0]:
            result.append(numsA[0])
            numsA = numsA[1:]
        else:
            result.append(numsB[0])
            numsB = numsB[1:]
    result += numsA
    result += numsB
    return result


def mergeSort(nums):
    if len(nums) <= 1:
        print(*nums)
        return nums
    mergedNums = merge(mergeSort(nums[:(len(nums) + 1) // 2]), mergeSort(nums[(len(nums) + 1) // 2:]))
    print(*mergedNums)
    return mergedNums


n = int(input())
listOfNums = list(map(int, input().split()))
mergeSort(listOfNums)
