"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_str_by_newline, parseInstruction


def runProgram(instr, vars={"w": 0, "x": 0, "y": 0, "z": 0,}):
    for (inst, to, v) in instr:
        if type(v) is str:
            v = vars[v]
        if inst == "add":
            vars[to] += v
        elif inst == "mul":
            vars[to] *= v
        elif inst == "div":
            vars[to] //= v
        elif inst == "mod":
            vars[to] = vars[to] % v
        elif inst == "eql":
            vars[to] = 1 if vars[to] == v else 0
    return vars["y"], vars["z"]


def solution_1(digitInstr):
    vars = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    outcomes = {0: ""}

    for digits in digitInstr:
        newOutcomes = {}
        prevY = 0
        y = 0
        for i in range(1, 10):
            for z in outcomes:
                vars = {
                    "w": i,
                    "x": z % 26,
                    "y": prevY,
                    "z": z,
                }
                prevDigits = outcomes[z]
                y, z = runProgram(digits, vars)
                if z < 100000:
                    newOutcomes[z] = prevDigits + str(i)
            prevY = y
        outcomes = newOutcomes
    max = 0
    for o in outcomes:
        if o == 0:
            num = int(outcomes[o])
            print(num)
            if num > max:
                max = num
    return max


def solution_2(digitInstr):
    vars = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    outcomes = {0: ""}

    for digits in digitInstr:
        newOutcomes = {}
        prevY = 0
        y = 0
        for i in range(9, 0, -1):
            for z in outcomes:
                vars = {
                    "w": i,
                    "x": z % 26,
                    "y": prevY,
                    "z": z,
                }
                prevDigits = outcomes[z]
                y, z = runProgram(digits, vars)
                if z < 100000:
                    newOutcomes[z] = prevDigits + str(i)
            prevY = y
        outcomes = newOutcomes
    min = 99999999999999
    for o in outcomes:
        if o == 0:
            num = int(outcomes[o])
            print(num)
            if num < min:
                min = num
    return min


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [
        [parseInstruction(l) for l in split_str_by_newline(d)]
        for d in input.split("inp w\nmul x 0\nadd x z\nmod x 26\n")[1:]
    ]
    # print(parsed_input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")
    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
