"""TEST MODULE TEMPLATE"""
from src.day16 import solution_1
from src.day16 import solution_2
import unittest


class TestAOCDay16(unittest.TestCase):
    def test_solution_1(self):
        example_input = [
            "8A004A801A8002F478",
            "620080001611562C8802118E34",
            "C0015000016115A2E0802F182340",
            "A0016C880162017C3686B18A3D4780"
        ]
        example_result = [
            16,12,23,31
        ]
        for i, _ in enumerate(example_input):
            self.assertEqual(solution_1(example_input[i]), example_result[i])

    def test_solution_2(self):
        example_input = []
        example_result = []
        for i, _ in enumerate(example_input):
            self.assertEqual(solution_2(example_input[i]), example_result[i])


if __name__ == "__main__":
    unittest.main()
