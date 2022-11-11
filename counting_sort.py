def counting_sort(array):
    result = []
    count = [0] * 10
    for i in array:
        count[i] += 1

    for d in range(10):
        result += [d] * count[d]

    return result


print(counting_sort([5, 2, 8, 3, 1, 4, 5, 9, 5, 1, 4, 5, 6, 7, 1, 1]))
