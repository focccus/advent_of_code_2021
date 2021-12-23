"""TEST MODULE TEMPLATE"""
from src.day22 import solution_1
from src.day22 import solution_2
import unittest


class TestAOCDay22(unittest.TestCase):
    def test_solution_1(self):
        example_input = []
        example_result = []
        for i, _ in enumerate(example_input):
            self.assertEqual(solution_1(example_input[i]), example_result[i]) 

    def test_solution_2(self):
        example_input = []
        example_result = []
        for i, _ in enumerate(example_input):
            self.assertEqual(solution_2(example_input[i]), example_result[i]) 


if __name__ == "__main__":
    unittest.main()
