"""TEST MODULE TEMPLATE"""
from src.day12 import solution,buildNeighborTable
import unittest

example_inputs = [
    [
        ("start", "A"),
        ("start", "b"),
        ("A", "c"),
        ("A", "b"),
        ("b", "d"),
        ("A", "end"),
        ("b", "end"),
    ],
    [
        ("dc", "end"),
        ("HN", "start"),
        ("start", "kj"),
        ("dc", "start"),
        ("dc", "HN"),
        ("LN", "dc"),
        ("HN", "end"),
        ("kj", "sa"),
        ("kj", "HN"),
        ("kj", "dc"),
    ],
    [
        ("fs", "end"),
        ("he", "DX"),
        ("fs", "he"),
        ("start", "DX"),
        ("pj", "DX"),
        ("end", "zg"),
        ("zg", "sl"),
        ("zg", "pj"),
        ("pj", "he"),
        ("RW", "he"),
        ("fs", "DX"),
        ("pj", "RW"),
        ("zg", "RW"),
        ("start", "pj"),
        ("he", "WI"),
        ("zg", "he"),
        ("pj", "fs"),
        ("start", "RW"),
    ],
]


class TestAOCDay12(unittest.TestCase):
    def test_solution_1(self):
        example_results = [10, 19, 226]
        for i, _ in enumerate(example_inputs):
            self.assertEqual(solution(buildNeighborTable(example_inputs[i])), example_results[i])

    def test_solution_2(self):
        example_results = [36, 103, 3509]
        for i, _ in enumerate(example_inputs):
            self.assertEqual(solution(buildNeighborTable(example_inputs[i]),2), example_results[i])


if __name__ == "__main__":
    unittest.main()
