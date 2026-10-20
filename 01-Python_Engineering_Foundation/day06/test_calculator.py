"""
Unit testing lets us check these cases automatically, so we can detect bugs when code changes.

For example:
Test case	        Input	    Expected result
Normal numbers	    10, 20	        30
Negative number	    -5, 3	        -2
Zero	            0, 0	        0
Python's built-in unittest framework lets us automate these checks without installing an additional package.
"""
import unittest

from calculator import add_numbers, subtract_numbers

class Test_Calculator(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(10, 20)
        self.assertEqual(result, 30)

    def test_subtract_numbers(self):
        result = subtract_numbers(10, 5)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -3), -8)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract_numbers(-5, -3), -2)

    # def test_intentional_failure_demo(self):
    #     self.assertEqual(add_numbers(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
