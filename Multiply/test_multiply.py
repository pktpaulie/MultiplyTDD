"""Using the pytest method for unit testing"""


from multiply import multiply, multiply_new


def test_multiply_1():
    """calling the assert function"""

    assert multiply(1, 1) == 1


def test_multiply_2():
    """calling the assert function"""
    assert multiply(2, 2) == 4


def test_multiply_3():
    """calling the assert function"""
    assert multiply(3, 3) == 9


def test_multiply_4():
    """calling the assert function"""
    assert multiply(4, 4) == 16


def test_multiply_5():
    """calling the assert function"""
    assert multiply(23, 45) == 1035


def test_multiply_6():
    """calling the assert function"""

    assert multiply(-1, -2) == 2  # test negative numbers


def test_multiply_7():
    """calling the assert function"""

    assert multiply(-3, 10) == -30  # test one negative number


def test_multiply_new():
    """
    calling the assert function to test the
    second multiply function
    """
    assert multiply_new(30, 0) == 0


def test_multiply_new_1():
    """
    calling the assert on second multiply function
    """
    assert multiply_new(-3, 3) == -9  # passes for one negative number


def test_multiply_new_2():
    """
    calling the assert on second multiply function
    """
    assert multiply_new(15, 10) == 150


def test_multiply_new_3():
    """
    calling the assert on second multiply function
    """
    assert multiply_new(24, 24) == 576
