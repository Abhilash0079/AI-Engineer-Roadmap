import unittest
from student_scores import calculate_average

class TestStudentScores(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90.0)

    def test_empty_scores(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_invalid_scores(self):
        with self.assertRaises(ValueError):
            calculate_average([80, "abc", 100])

    def test_boolean_scores(self):
        with self.assertRaises(ValueError):
            calculate_average([80, True, 100])

if __name__=='__main__':
    unittest.main()
