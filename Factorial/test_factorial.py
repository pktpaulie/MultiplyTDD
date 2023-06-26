"""Code to test factorial function"""

import pytest
from factorial import find_factorial


@pytest.mark.filterwarnings # trying out the pytest markers
def test_factorial_true():
    """Call assert function for different test cases """

    assert find_factorial(0) == 1
    assert find_factorial(5) == 120
    assert find_factorial(8) == 40320
