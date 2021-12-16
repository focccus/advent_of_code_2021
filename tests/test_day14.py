"""TEST MODULE TEMPLATE"""
from src.day14 import solution, polymerStep
import unittest

example_template = "NNCB"

example_rules = {
    "CH": "B",
    "HH": "N",
    "CB": "H",
    "NH": "C",
    "HB": "C",
    "HC": "B",
    "HN": "C",
    "NN": "C",
    "BH": "H",
    "NC": "B",
    "NB": "B",
    "BN": "B",
    "BB": "N",
    "BC": "B",
    "CC": "N",
    "CN": "C",
}


class TestAOCDay14(unittest.TestCase):
    def test_steps(self):
        example_steps = [
            "NCNBCHB",
            "NBCCNBBBCBHCB",
            "NBBBCNCCNBBNBNBBCHBHHBCHB",
            "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB",
        ]
        t = example_template
        for s in example_steps:
            t = polymerStep(t, example_rules)
            self.assertEqual(t, s)
    def test_solution_1(self):
        example_result = 1588
        self.assertEqual(solution(example_template, example_rules), example_result)

    def test_solution_2(self):
        example_result = 2188189693529
        self.assertEqual(solution(example_template, example_rules,40), example_result)


if __name__ == "__main__":
    unittest.main()
