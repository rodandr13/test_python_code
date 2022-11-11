def is_simple_number(number):
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


assert is_simple_number(4) == True
assert is_simple_number(20) == False

