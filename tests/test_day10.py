"""TEST MODULE TEMPLATE"""
from src.day10 import solution_1
from src.day10 import solution_2
import unittest

example_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


class TestAOCDay10(unittest.TestCase):
    def test_solution_1(self):
        example_result = 2 * 3 + 57 + 1197 + 25137

        self.assertEqual(solution_1(example_input), example_result)

    def test_solution_2(self):
        example_result = 288957

        self.assertEqual(solution_2(example_input), example_result)


if __name__ == "__main__":
    unittest.main()
