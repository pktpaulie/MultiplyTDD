"""Using the pytest method for unit testing"""


from multiply import multiply, multiply_new

def test_multiply_1():
    """calling the assert function"""

    assert multiply(1, 1) == 1
    assert multiply(2, 2) == 4
    assert multiply(3, 3) == 9
    assert multiply(4, 4) == 16
    assert multiply(23, 45) == 1035



def test_multiply_new():
    """
    calling the assert function to test the 
    second multiply function
    """

    assert multiply_new(-3, 3) == -9
