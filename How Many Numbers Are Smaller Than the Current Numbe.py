def smallnumber(arr):
    c = 0
    lister = []
    for i in range(len(arr)):
        c = 0
        for k in range(len(arr)):
            if arr[i] > arr[k]:
                c += 1
        lister.append(c)
    print(lister)
    return lister


arr = [8, 1, 2, 2, 3]
smallnumber(arr)
