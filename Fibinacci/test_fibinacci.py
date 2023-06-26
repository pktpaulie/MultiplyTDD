"""
Function to test the fibinacci solution in fibinacci.py
"""

from fibinacci import fibinacci_1, fibinacci_2


def test_fibinacci():
    """call the assert function to test if our fibinacci function is true"""

    assert fibinacci_1(1) == 0  # test on basic function to pass the test
    assert fibinacci_2(1) == 0  # test on improved function
    assert fibinacci_2(2) == 1
    assert fibinacci_2(4) == 2
    assert fibinacci_2(6) == 5
    assert fibinacci_2(8) == 13
    assert fibinacci_2(10) == 34
    assert fibinacci_2(14) == 233