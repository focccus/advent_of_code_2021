"""TEST MODULE TEMPLATE"""
from src.day06 import solution
import unittest

example_input = [3, 4, 3, 1, 2]


class TestAOCDay06(unittest.TestCase):
    def test_solution_1(self):

        example_result = 5934

        self.assertEqual(solution(example_input), example_result)

    def test_solution_2(self):
        example_result = 26984457539

        self.assertEqual(solution(example_input,256), example_result)


if __name__ == "__main__":
    unittest.main()
