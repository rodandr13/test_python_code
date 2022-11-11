def sieve_of_eratosthenes(array):
    array = [True] * len(array)
    array[0] = array[1] = None
    for i in range(2, len(array)):
        if array[i]:
            for j in range(2*i, len(array), i):
                array[j] = False
    for i in range(len(array)):
        print(i, '-', 'простое' if array[i] else 'составное')


sieve_of_eratosthenes(range(35))
