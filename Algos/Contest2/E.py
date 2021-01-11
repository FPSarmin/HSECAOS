from sys import stdin


def selectionSort(arr, k):
    for i in range(k):
        minpos = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minpos]:
                minpos = j
        (arr[minpos], arr[i]) = (arr[i], arr[minpos])
    return arr


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
print(*selectionSort(arr, int(stdin.readline())))

