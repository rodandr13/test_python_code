""""
Проверка скобочной последовательности на корректность
"""


def braces_sequence(s):
    stack = []
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            stack.append(brace)
        else:
            if len(stack) == 0:
                 return False
            left = stack.pop()
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return len(stack) == 0


s1 = "(([]]))"
s2 = "([])[(((())))][]"
assert braces_sequence(s1) == False
assert braces_sequence(s2) == True
