"""TEST MODULE TEMPLATE"""
from src.day20 import solution, parse01Line
import unittest
import numpy as np


example_alg = parse01Line(
    "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
)
example_img = np.array(
    [
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1],
    ]
)


class TestAOCDay20(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(solution(example_alg,example_img), 35)

    def test_solution_2(self):
        example_result = 3351
        self.assertEqual(solution(example_alg,example_img,50), example_result)


if __name__ == "__main__":
    unittest.main()
