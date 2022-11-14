def left_bound(A, key):
    left = -1
    right = len(A)

    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    left = -1
    right = len(A)

    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


array = [1, 1, 1, 1, 2, 2, 4, 4, 7, 7]
print(left_bound(array, 7))
print(right_bound(array, 7))
