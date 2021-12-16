"""TEST MODULE TEMPLATE"""
from src.day15 import solution_1
from src.day15 import solution_2
import unittest
import numpy as np

example_input = np.array([
    [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
    [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
    [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
    [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
    [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
    [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
    [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
    [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
    [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
    [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
])


class TestAOCDay15(unittest.TestCase):
    def test_solution_1(self):
        example_result = 40

        self.assertEqual(solution_1(example_input), example_result)

    def test_solution_2(self):
        example_input = []
        example_result = []
        for i, _ in enumerate(example_input):
            self.assertEqual(solution_2(example_input[i]), example_result[i])


if __name__ == "__main__":
    unittest.main()
