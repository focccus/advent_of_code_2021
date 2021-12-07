"""TEST MODULE TEMPLATE"""
from src.day07 import solution
import unittest

example_input = [16,1,2,0,4,2,7,1,2,14]

class TestAOCDay07(unittest.TestCase):
    def test_solution_1(self):
        example_result = 37

        self.assertEqual(solution(example_input), example_result) 

    def test_solution_2(self):

        example_result = 168
        self.assertEqual(solution(example_input, False), example_result) 


if __name__ == "__main__":
    unittest.main()
