F = [None] * 10000


def fibonacci(n):
    if F[n] is None:
        if n < 1:
            F[n] = 1
        else:
            F[n] = fibonacci(n-1) + fibonacci(n-2)
    return F[n]


print(fibonacci(100))
