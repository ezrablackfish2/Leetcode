def sentece_sorter(s):
    arr = s.split()
    final = ""
    for i in range(len(arr)):
        minimum_index = i
        for j in range(i + 1, len(arr)):
            if arr[j][-1] < arr[minimum_index][-1]:
                minimum_index = j
        if minimum_index != i:
            temp = arr[minimum_index]
            arr[minimum_index] = arr[i]
            arr[i] = temp
        final += arr[i][:-1] + " "
    print(final[:-1])
    return final


s = "is2 sentence4 This1 a3"
sentece_sorter(s)
