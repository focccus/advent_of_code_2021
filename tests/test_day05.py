"""TEST MODULE TEMPLATE"""
from src.day05 import solution
import unittest

example_input = [
    [0, 9, 5, 9],
    [8, 0, 0, 8],
    [9, 4, 3, 4],
    [2, 2, 2, 1],
    [7, 0, 7, 4],
    [6, 4, 2, 0],
    [0, 9, 2, 9],
    [3, 4, 1, 4],
    [0, 0, 8, 8],
    [5, 5, 8, 2],
]


class TestAOCDay05(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(solution(example_input), 5)

    def test_solution_2(self):
        self.assertEqual(solution(example_input, True), 12)


if __name__ == "__main__":
    unittest.main()
