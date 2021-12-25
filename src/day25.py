"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_str_by_newline


def printField(field):
    tostr = ".>v"
    print("")
    for row in field:
        print("".join(tostr[i] for i in row))


def stepRight(input):
    newInput = []
    for row in input:
        newInput.append([0] * len(row))
        for i, col in enumerate(row):
            pos = (i + 1) % len(row)
            if col == 1 and row[pos] == 0:
                newInput[-1][pos] = 1
                newInput[-1][i] = 0
            elif newInput[-1][i] == 0:
                newInput[-1][i] = col
    return newInput


def stepDown(input):
    newInput = []
    newInput.append([0] * len(input[0]))
    for i, row in enumerate(input):
        newInput.append([0] * len(row))
        pos = (i + 1) % len(input)
        for j, col in enumerate(row):
            if col == 2 and input[pos][j] == 0:
                newInput[pos][j] = 2
                newInput[i][j] = 0
            elif newInput[i][j] == 0:
                newInput[i][j] = col
    return newInput[:-1]


def solution_1(input):
    i = 0
    while True:
        ninput = stepRight(input)
        ninput = stepDown(ninput)
        i += 1
        if ninput == input:
            break
        input = ninput
    return i


def solution_2(input):
    pass


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
#     input = """v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>"""
    translate = {".": 0, ">": 1, "v": 2}
    parsed_input = [[translate[c] for c in l] for l in split_str_by_newline(input)]

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
