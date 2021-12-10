"""Solution module for Day X, YEAR"""
import copy
import time
from functools import reduce

from utils.fetch import fetch
from utils.parse import split_str_by_newline

closingMap = {"(": ")", "[": "]", "{": "}", "<": ">"}
corr_scoreMap = {"": 0, ")": 3, "]": 57, "}": 1197, ">": 25137}


def check_chunk(line: str):
    stack = []
    for c in line:
        if c in closingMap:
            stack.append(closingMap[c])
        elif stack[-1] != c:
            # check if correct
            return c
        else:
            # pop all correct ones
            stack.pop()
    # stack contains missing in reverse order
    stack.reverse()
    return "".join(stack)


def solution_1(input):
    score = 0
    for l in input:
        err = check_chunk(l)
        if len(err) == 1:
            score += corr_scoreMap[err]
    return score


incom_scoreMap = {"": 0, ")": 1, "]": 2, "}": 3, ">": 4}


def solution_2(input):
    scores = []
    for l in input:
        err = check_chunk(l)
        if len(err) > 1:
            scores.append(reduce(lambda acc, x: acc * 5 + incom_scoreMap[x], err, 0))
    scores.sort()
    return scores[len(scores) // 2]


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
