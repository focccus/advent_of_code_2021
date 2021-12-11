"""TEST MODULE TEMPLATE"""
from src.day11 import solution_1
from src.day11 import solution_2
import unittest
import numpy as np

example_input = np.array(
    [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]
)


class TestAOCDay11(unittest.TestCase):
    def test_solution_1(self):
        example_result = 1656

        self.assertEqual(solution_1(example_input), example_result)

    def test_solution_2(self):
        example_result = 195
        self.assertEqual(solution_2(example_input), example_result)


if __name__ == "__main__":
    unittest.main()
