"""TEST MODULE TEMPLATE"""
from src.day01 import solution_1
from src.day01 import solution_2
import unittest


class TestAOCDay01(unittest.TestCase):
    def test_solution_1(self):
        example_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        example_result = 7
        
        self.assertEqual(solution_1(example_input), example_result)

    def test_solution_2(self):
        example_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        example_result = 5
        
        self.assertEqual(solution_2(example_input), example_result)


if __name__ == "__main__":
    unittest.main()
