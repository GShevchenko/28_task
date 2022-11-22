def squirrel(my_number: int) -> int:
    fact = factorial(my_number)
    return get_max_digit(fact)


def factorial(my_number: int) -> int:
    if my_number == 0:
        return 1
    fact = 1
    for i in range(2, my_number + 1):
        fact *= i
    return fact


def get_max_digit(my_number: int) -> int:
    result = my_number
    while my_number > 9:
        result = my_number // 10
        my_number = result
    return result
