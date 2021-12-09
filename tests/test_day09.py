"""TEST MODULE TEMPLATE"""
from src.day09 import solution_1
from src.day09 import solution_2
import unittest

example_input = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]


class TestAOCDay09(unittest.TestCase):
    def test_solution_1(self):
        example_result = 15
        
        self.assertEqual(solution_1(example_input), example_result)

    def test_solution_2(self):
        example_result = [9,9,14]
        
        self.assertEqual(solution_2(example_input), example_result)


if __name__ == "__main__":
    unittest.main()
