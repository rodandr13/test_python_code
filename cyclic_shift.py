def cyclic_shift(array):
    tmp = array[0]
    for i in range(len(array) - 1):
        array[i] = array[i+1]
    array[len(array)-1] = tmp

    return array


array = [1, 2, 3, 4, 5]
print(cyclic_shift(array))
