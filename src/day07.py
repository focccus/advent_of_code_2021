"""Solution module for Day X, YEAR"""
import copy
import time
import numpy as np

from utils.fetch import fetch
from utils.parse import split_number_by_separator


def calculate_fuel(distances, constant=True):
    if constant:
        return np.sum(distances)

    # using sum formula 1 + 2 + ... + n = n * (n+1)/2
    return int(np.sum(distances * (distances + 1) / 2))


def solution(input, constant=True):
    crabs = np.array(input)
    max = np.max(crabs)

    return min([calculate_fuel(np.abs(crabs - i), constant) for i in range(max)])


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_separator(input, ",")

    tic = time.perf_counter()
    s1 = solution(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution(copy.deepcopy(parsed_input), False)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
