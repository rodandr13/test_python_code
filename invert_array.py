def invert_array(array):
    length = len(array)
    for i in range(length // 2):
        array[i], array[length-1-i] = array[length-1-i], array[i]
    return array


array = [1, 2, 3, 4, 5]
result = [5, 4, 3, 2, 1]

assert invert_array(array) == result
