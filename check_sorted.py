def check_sorted(array, ascending=True):
    for i in range(len(array) - 1):
        if (array[i] < array[i + 1]) != ascending:
            return False
    return True


print(check_sorted([1, 2, 3, 4]))
