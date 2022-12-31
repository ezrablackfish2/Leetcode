def countSwaps(a):
    i = 0
    j = 1
    w = 0
    counter = 0
    if j == len(a) - 1:
        counter1(a)
    elif i == 0:
        counter2(a)
    print(counter)
    return counter


def counter1(a):
    i = len(a) - 2
    j = len(a) - 1
    w = 0
    counter = 0
    for k in a:
        if a[i] > a[j]:
            w = a[i]
            a[i] = a[j]
            a[j] = a[i]
            counter += 1
        j = j - 1
        i = i - 1
        if j == len(a) - 1:
            counter2(a)
    return counter


def counter2(a):
    i = 0
    j = 1
    for k in a:
        if a[i] > a[j]:
            w = a[i]
            a[i] = a[j]
            a[j] = a[i]
            counter += 1
        j = j + 1
        i = i + 1
        if i == 0:
            counter1(a)
    return counter


a = [3, 6, 3, 7]
countSwaps(a)
