def bubble_sort(array):
    for bypass in range(1, len(array)):
        for k in range(0, len(array) - bypass):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]
    return array


print(bubble_sort([4, 2, 5, 1, 3]))
print(bubble_sort([4, 4, 5, 1, 1]))
