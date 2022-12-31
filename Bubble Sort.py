#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    i, j, temp, counter, = (
        0,
        0,
        0,
        0,
    )
    while i < len(a):
        if i == 0:
            i += 1
            continue
        if a[i] < a[i - 1]:
            j = i
            while j > 0 and a[j] <= a[j - 1]:
                temp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = temp
                counter += 1
                j -= 1
        i += 1
    print("Array is sorted in {} swaps.".format(counter))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
    return counter


if __name__ == "__main__":

    a = [3, 2, 1]

    countSwaps(a)
