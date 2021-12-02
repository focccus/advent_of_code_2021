"""TEST MODULE TEMPLATE"""
from src.day02 import solution_1
from src.day02 import solution_2
import unittest


class TestAOCDay02(unittest.TestCase):
    def test_solution_1(self):
        example_input = [("f", 5), ("d", 5), ("f", 8), ("u", 3), ("d", 8), ("f", 2)]
        example_result = 150

        self.assertEqual(solution_1(example_input), example_result)

    def test_solution_2(self):
        example_input = [("f", 5), ("d", 5), ("f", 8), ("u", 3), ("d", 8), ("f", 2)]
        example_result = 900

        self.assertEqual(solution_2(example_input), example_result)


if __name__ == "__main__":
    unittest.main()
