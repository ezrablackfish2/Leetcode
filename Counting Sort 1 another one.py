def countingSort(arr):
    lister = [0] * len(arr)
    for k in arr:
        lister[k] += 1
    print(*lister)
    return lister


arr = [2, 1, 2, 1, 3, 2]
countingSort(arr)
