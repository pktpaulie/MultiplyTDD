"""method to test the multiply function"""

import unittest

from multiply import multiply


class MultiplyTest(unittest.TestCase):
    """multiply unit test"""
    

    def test_multiply(self):
        """calling the assertEqual function"""
        

        self.assertEqual(multiply(3, 3), 9)