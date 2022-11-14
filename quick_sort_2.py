def quick_sort(array):
    if len(array) <= 1:
        return
    barrier = array[0]
    L = []
    M = []
    R = []
    for x in array:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in L + M + R:
        array[k] = x
        k += 1


array = [7, 1, 2, 1, 4, 7, 1, 2, 1, 4]
print(array)
quick_sort(array)
print(array)

