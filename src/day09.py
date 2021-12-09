"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_str_by_newline


def neighbors(matrix, i, j):
    return [
        matrix[n][m]
        for (n, m) in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
        if n >= 0 and m >= 0 and n < len(matrix) and m < len(matrix[0])
    ]


def lowpoints(matrix):
    return [
        (i, j)
        for i in range(len(matrix))
        for j in range(len(matrix[i]))
        if matrix[i][j] < min(neighbors(matrix, i, j))
    ]


def count_basin(matrix, i, j):
    if matrix[i][j] >= 9:
        return 0
    matrix[i][j] = 9
    return 1 + sum(
        count_basin(matrix, n, m)
        for (n, m) in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
        if n >= 0 and m >= 0 and n < len(matrix) and m < len(matrix[0])
    )


def solution_1(input):
    return sum(input[i][j] + 1 for (i, j) in lowpoints(input))


def solution_2(input):
    lp = lowpoints(input)
    return sorted(count_basin(input, i, j) for (i, j) in lp)[-3:]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [list(map(int, l)) for l in split_str_by_newline(input)]

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(
        f"Solution for problem 2: {s2[0] * s2[1] * s2[2]}, acquired in: {toc-tic:0.4f} seconds"
    )
