"""TEST MODULE TEMPLATE"""
from src.day04 import solution_1
from src.day04 import solution_2
import unittest

from utils.parse import parse_matrix

example_input = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]
example_boards = [
    parse_matrix(
        """22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19"""
    ),
    parse_matrix(
        """ 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6"""
    ),
    parse_matrix(
        """14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    ),
]

print(example_boards)


class TestAOCDay04(unittest.TestCase):
    def test_solution_1(self):
        example_result = 188 * 24
        self.assertEqual(solution_1(example_input, example_boards), example_result)

    def test_solution_2(self):
        example_result = 148 * 13

        self.assertEqual(solution_2(example_input, example_boards), example_result)


if __name__ == "__main__":
    unittest.main()
