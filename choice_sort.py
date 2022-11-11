def choice_sort(array):
    for pos in range(0, len(array) - 1):
        for k in range(pos + 1, len(array)):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]
    return array


print(choice_sort([4, 2, 5, 1, 3]))
print(choice_sort([4, 4, 5, 1, 1]))
