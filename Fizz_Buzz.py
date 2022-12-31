# class Solution(object)
def fizzBuzz(n):
    a = 1
    lister = []
    while a != n:
        if a % 3 == 0:
            b = "fizz"
            lister.append(b)
        elif a % 5 == 0:
            b = "Buzz"
            lister.append(b)
        else:
            b = a
            lister.append(b)
        a += 1
    print(lister)
    return lister


fizzBuzz(15)
