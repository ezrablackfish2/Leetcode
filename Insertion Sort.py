def insertionSort1(n, arr):
    i = len(arr) - 1
    e = arr[-1]
    while e <= arr[i - 1] and i >= 0:
        if i == 0:
            arr[i] = e
            break
        else:
            if e <= arr[i - 1]:
                arr[i] = arr[i - 1]
                print(*arr)
            i -= 1
    if e > arr[i - 1]:
        arr[i] = e
    print(*arr)
    print(e)
    return arr


arr = [1, 2, 3, 6, 9, 0]
insertionSort1(15, arr)
