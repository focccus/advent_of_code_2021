"""Solution module for Day X, YEAR"""
import copy
import time
import math
import re

from utils.fetch import fetch
from utils.parse import parse_all_numbers


def simulate(initial, target):
    x = y = 0
    v = initial

    maxY = 0
    traj = []
    # stop when shot above y bounds
    while y >= target[2]:
        x += v[0]
        y += v[1]
        if initial == (6, 0):
            traj.append((x, y))
        maxY = max(maxY, y)
        if v[0] == 0:
            v = (0, v[1] - 1)
        else:
            v = (v[0] - v[0] / abs(v[0]), v[1] - 1)
        # case: shot above x bounds
        if abs(x) > abs(target[1]):
            return -2
        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            return maxY
    # did not reach target
    return -1


# Calculate X so v[0] is 0 at goal
def calcX(goal):
    return -1 / 2 + math.sqrt(1 / 4 + goal * 2)


def solution_1(target):
    minX = math.ceil(calcX(target[0]))
    maxX = math.floor(calcX(target[1]))
    maxY = 0
    for x in range(minX, maxX + 1):
        # bruteforce y
        for y in range(1, 200):
            val = simulate((x, y), target)
            maxY = max(maxY, val)
    return maxY


def solution_2(target):
    minX = math.ceil(calcX(target[0]))
    maxX = target[1]
    minY = target[2]
    count = 0
    for x in range(minX, maxX + 1):
        for y in range(minY, 200):
            val = simulate((x, y), target)
            if val >= 0:
                count += 1
    return count


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = tuple(parse_all_numbers(input))

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
