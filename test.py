"""method to test the multiply function using the built in unittest method"""

import unittest

from multiply import multiply


class MultiplyTest(unittest.TestCase):
    """multiply unit test"""

    def test_multiply(self):
        """calling the assertEqual function"""

        self.assertEqual(multiply(23, 45), 23 * 45)


if __name__ == "__main__":
    unittest.main()  # To run this file directly
