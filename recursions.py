def recursion(n):
    if n == 0:
        print("Конец")
    else:
        print(n)
        recursion(n-1)
        print(n)


def f(n):
    if n == 0:
        return 1
    return f(n-1) * n


recursion(5)
print(f(5))
