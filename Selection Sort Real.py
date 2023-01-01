def smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newarr = []
    for i in range(len(arr)):
        small = smallest(arr)
        popper = arr.pop(small)
        newarr.append(popper)
    print(newarr)
    return newarr


arr = [4, 1, 9, 3, 9, 7]
selectionsort(arr)
