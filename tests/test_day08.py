"""TEST MODULE TEMPLATE"""
from src.day08 import solution_1
from src.day08 import solution_2
import unittest


example_input = [
    [
        "be",
        "abcdefg",
        "bcdefg",
        "acdefg",
        "bceg",
        "cdefg",
        "abdefg",
        "bcdef",
        "abcdf",
        "bde",
        "abcdefg",
        "bcdef",
        "bcdefg",
        "bceg",
    ],
    [
        "abdefg",
        "bcdeg",
        "bcg",
        "cg",
        "abcdefg",
        "bdefg",
        "abcdfg",
        "abcde",
        "bcdefg",
        "cefg",
        "bcdefg",
        "bcg",
        "abcdefg",
        "cg",
    ],
    [
        "abdefg",
        "cg",
        "abcde",
        "abdfg",
        "abcdfg",
        "bcdefg",
        "abcdg",
        "acfg",
        "bcg",
        "abcdefg",
        "cg",
        "cg",
        "abcdfg",
        "bcg",
    ],
    [
        "bcdefg",
        "bcd",
        "abcdef",
        "abdeg",
        "abcf",
        "bc",
        "acdef",
        "abcde",
        "acdefg",
        "abcdefg",
        "abcdef",
        "abcde",
        "acdefg",
        "bc",
    ],
    [
        "abcdefg",
        "bfg",
        "fg",
        "abefg",
        "abdef",
        "cefg",
        "abceg",
        "abcefg",
        "abcdeg",
        "abcdfg",
        "cefg",
        "abcdefg",
        "bfg",
        "abefg",
    ],
    [
        "abefg",
        "ac",
        "abcefg",
        "abcdefg",
        "acdefg",
        "bcdfg",
        "abce",
        "abdefg",
        "abcfg",
        "acf",
        "abcdefg",
        "abce",
        "ac",
        "abcdefg",
    ],
    [
        "bcdfg",
        "dfg",
        "abcdefg",
        "cefg",
        "abdefg",
        "abcdef",
        "bcdef",
        "abcdg",
        "bcdefg",
        "fg",
        "cefg",
        "bcdef",
        "cefg",
        "abcdefg",
    ],
    [
        "bcdefg",
        "abcefg",
        "bcefg",
        "acdefg",
        "abcdg",
        "de",
        "bdef",
        "cde",
        "abcdefg",
        "bcdeg",
        "de",
        "abcefg",
        "abcdg",
        "bcefg",
    ],
    [
        "abdefg",
        "bcdefg",
        "cdeg",
        "abcef",
        "bcg",
        "abcdefg",
        "cg",
        "abcdfg",
        "bdefg",
        "bcefg",
        "abcdefg",
        "bcg",
        "cg",
        "bcg",
    ],
    [
        "abcfg",
        "cfg",
        "abcdefg",
        "abceg",
        "fg",
        "abcdeg",
        "aefg",
        "abcefg",
        "abcdf",
        "bcdefg",
        "aefg",
        "abcfg",
        "fg",
        "abceg",
    ],
]


class TestAOCDay08(unittest.TestCase):
    def test_solution_1(self):
        example_result = 26
        self.assertEqual(solution_1(example_input), example_result)

    def test_solution_2(self):
        example_result = 61229
        self.assertEqual(solution_2(example_input), example_result)


if __name__ == "__main__":
    unittest.main()