"""TEST MODULE TEMPLATE"""
from src.day17 import solution_1
from src.day17 import solution_2
import unittest

example_input = (20,30,-10,-5)

class TestAOCDay17(unittest.TestCase):
    def test_solution_1(self):
        example_result = 45
        self.assertEqual(solution_1(example_input), example_result) 

    def test_solution_2(self):
        example_result = 112
        
        self.assertEqual(solution_2(example_input), example_result) 


if __name__ == "__main__":
    unittest.main()
