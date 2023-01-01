def selectionsort(arr):
    i = 0
    j = 0
    temp = 0
    while i < len(arr):
        if i == 0:
            i += 1
        if arr[i] < arr[i - 1]:
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                j -= 1
        i += 1
    print(*arr)
    return arr


arr = [4, 1, 3, 9, 7]
selectionsort(arr)
