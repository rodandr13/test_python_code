stack = []


def push(x):
    stack.append(x)


def pop():
    return stack.pop()


def clear():
    stack.clear()


def is_empty():
    return len(stack) == 0

