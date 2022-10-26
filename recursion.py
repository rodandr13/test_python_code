# Тесты рекурсий

def factorial(x):
    if x == 1:
        return 1
    else:
        print(x)
        return x * factorial(x - 1)


print(factorial(10))


def sum1(array):
    if len(array) <= 1:
        return array[0]
    return array[0] + sum1(array[1:])


print(sum1([1, 2, 3, 4, 5]))


def find_smallest(array):
    if len(array) <= 1:
        return array[0]
    m = find_smallest(array[1:])
    return m if m < array[0] else array[0]


print('find_smallest')
print(find_smallest([5, 2, 7, 1, 2]))
'''
def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest_index = array[i]
            smallest_index = i
    return smallest_index
'''