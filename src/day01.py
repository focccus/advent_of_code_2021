"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_number_by_newline


def solution_1(input):
    return sum(elem[1] > elem[0] for elem in zip(input, input[1:]))


def solution_2(input):
    sums = map(sum, zip(input, input[1:],input[2:]))
    return solution_1(list(sums))


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
