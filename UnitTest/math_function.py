# Module

def modulo_function(number: int) -> int:
    """
    :param number: number
    :return: The number % 2.
    """
    result = number % 2
    return result


def is_even(number: int) -> bool:
    """
    :param number: number
    :return: True if the number is even, else False.
    """
    return number % 2 == 0


def is_odd(number: int) -> bool:
    """
    :param number: number
    :return: True if the number is odd, else False.
    """
    return number % 2 != 0


def sum_function(num_a, num_b):
    return num_a + num_b


def sub_function(num_a, num_b):
    return num_a - num_b


def mul_function(num_a, num_b):
    return num_a * num_b


def div_function(num_a, num_b):
    return num_a / num_b
