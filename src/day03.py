"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_number_by_newline, split_str_by_newline


def count_ones_column(input, i):
    ones = 0
    for line in input:
        if line[i] == "1":
            ones += 1
    return ones


def solution_1(input):
    n = len(input[0])
    ones = [count_ones_column(input, i) for i in range(0, n)]

    gamma = ""
    epsilon = ""
    for count in ones:
        if count >= len(input) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def solution_2(input):
    n = len(input[0])

    oxCandidates = input
    co2Candidates = input

    for i in range(0, n):
        moreZeros = count_ones_column(oxCandidates, i) < len(oxCandidates) / 2
        if len(oxCandidates) == 1:
            break
        oxCandidates = list(filter(lambda x: moreZeros ^ (x[i] == "1"), oxCandidates))
        
    for i in range(0, n):
        moreZeros = count_ones_column(co2Candidates, i) < len(co2Candidates) / 2
        if len(co2Candidates) == 1:
            break
        co2Candidates = list(filter(lambda x: moreZeros ^ (x[i] == "0"), co2Candidates))

    return int(oxCandidates[0], 2) * int(co2Candidates[0], 2)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
