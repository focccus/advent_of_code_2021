"""TEST MODULE TEMPLATE"""
from src.day13 import solution_1
from src.day13 import solution_2
import unittest

example_input = [
    (6, 10),
    (0, 14),
    (9, 10),
    (0, 3),
    (10, 4),
    (4, 11),
    (6, 0),
    (6, 12),
    (4, 1),
    (0, 13),
    (10, 12),
    (3, 4),
    (3, 0),
    (8, 4),
    (1, 10),
    (2, 14),
    (8, 10),
    (9, 0),
]
example_folds = [("y", 7), ("x", 5)]


class TestAOCDay13(unittest.TestCase):
    def test_solution_1(self):

        example_result = 17
        self.assertEqual(solution_1(example_input, example_folds), example_result)

    def test_solution_2(self):
        example_result = 16

        self.assertEqual(solution_2(example_input, example_folds), example_result)


if __name__ == "__main__":
    unittest.main()
