"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_number_by_newline, split_str_by_newline


def solution_1(input):
    depth = 0
    pos = 0
    for (i, val) in input:
        if i == "f":
            pos += val
        elif i == "d":
            depth += val
        elif i == "u":
            depth -= val
    return depth * pos


def solution_2(input):
    depth = 0
    pos = 0
    aim = 0
    for (i, val) in input:
        if i == "f":
            pos += val
            depth += aim * val
        elif i == "d":
            aim += val
        elif i == "u":
            aim -= val
    return depth * pos


def parseInstructionTuple(line: str):
    s = line.split(" ")
    return s[0][0], int(s[1])


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [parseInstructionTuple(s) for s in split_str_by_newline((input))]

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
