# Бинарный поиск по книге "Грокаем алгоритмы"

def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = list(range(0, 100))

print(binary_search(my_list, 88))
print(binary_search(my_list, -1))

