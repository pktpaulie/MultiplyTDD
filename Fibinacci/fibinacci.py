"""
Function to get the Fibinacci Sequence

where current = previous + (previous - 1)
xn = (xn - 1) + (xn - 2)
where xn is the next number in the sequence
The sequence starts at 0
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ......

Pair:
1. Pauline Korukundo
2. Malik Musumba

"""


def fibinacci_1(num):
    """Define a function that can pass the first test"""
    num = 0
    return num


def fibinacci_2(num):
    """
    Define the fibinacci sequence function
    Evolving the function to pass all testcases
    """

    result = 0
    counter = 1

    for x in range(1,num):  # x helps us to iterate over the loop
        temp_val = result
        result = result + counter
        counter = temp_val


    return result