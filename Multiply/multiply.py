"""Module to multiply numbers that will be tested"""


def multiply(var_a, var_b):
    """Function to multiply"""

    return var_a * var_b


def multiply_new(var_a, var_b):
    """
    Function to multiply two numbers using a for loop
    2 * 3 = 2 + 2 + 2
    """

    result = 0


    for x in range(var_b):
        if var_b < 0:
            result = result - var_a
        else:
            result = result + var_a

    return result
