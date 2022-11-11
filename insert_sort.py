def insert_sort(array):
    for top in range(1, len(array)):
        i = top
        while i > 0 and array[i-1] > array[i]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array


print(insert_sort([4, 2, 5, 1, 3]))
print(insert_sort([4, 4, 5, 1, 1]))
