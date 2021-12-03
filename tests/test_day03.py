"""TEST MODULE TEMPLATE"""
from src.day03 import solution_1
from src.day03 import solution_2
import unittest

example_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

class TestAOCDay03(unittest.TestCase):

    def test_solution_1(self):
        
        example_result = 9 * 22

        self.assertEqual(solution_1(example_input), example_result)

    def test_solution_2(self):
        example_result = 23 * 10

        self.assertEqual(solution_2(example_input), example_result)


if __name__ == "__main__":
    unittest.main()
