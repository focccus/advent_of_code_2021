"""Solution module for Day X, YEAR"""
import copy
import time
import math

from utils.fetch import fetch
from utils.parse import split_str_by_newline, parse_all_numbers


def cmp(a, b):
    return (a > b) - (a < b)


def points_inbetween(startend):
    points = []
    xdif = cmp(startend[2], startend[0])
    ydif = cmp(startend[3], startend[1])
    dstMax = max(xdif * (startend[2] - startend[0]), ydif * (startend[3] - startend[1]))

    for i in range(0, dstMax + 1):
        points.append((startend[0] + i * xdif, startend[1] + i * ydif))
    return points


def print_grid_plot(grid):
    for row in grid:
        print("".join(["{:2d}".format(n).replace("0", ".") for n in row]))


def solution(lines, vertical=False):

    print(points_inbetween([0, 10, 10, 0]))
    size = 1000
    grid = [0] * size ** 2
    for l in lines:
        if vertical or l[0] == l[2] or l[1] == l[3]:
            for p in points_inbetween(l):
                grid[p[0] + p[1] * (size - 1)] += 1
    return len([i for i in grid if i > 1])


def solution_2(input):
    pass


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [parse_all_numbers(line) for line in split_str_by_newline(input)]

    tic = time.perf_counter()
    s1 = solution(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution(copy.deepcopy(parsed_input), True)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
