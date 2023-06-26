"""
Module to define Factorial function

n! = n * (n-1) * (n-2) * .....3 * 2 * 1
n! = n * (n-1)!

Pair:
1. Pauline Korukundo
2. Malik Musumba

"""


def find_factorial(num_to_check):
    """Factorial function"""

    if num_to_check < 0:
        pass

    if num_to_check == 0:
        result = 1

    else:
        result = 1
        for i in range(1, (num_to_check + 1)):
            result = result * (i)
            # if num_to_check = 5
            # result = 1 * 1
            # result = 1 * 2
            # result = 2 * 3
            # result = 6 * 4
            # result = 24 * 5

    return result
