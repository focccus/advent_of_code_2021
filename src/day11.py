"""Solution module for Day X, YEAR"""
import copy
import time
import numpy as np

from utils.fetch import fetch
from utils.parse import parseIntMatrix


def increaseNeighbors(input: np.ndarray, i, j):
    c = 0
    for y in range(i - 1, i + 2):
        if 0 <= y < input.shape[0]:
            for x in range(j - 1, j + 2):
                if 0 <= x < input.shape[1]:
                    input[y, x] += 1
                    c += input[y, x] == 10
    input[i, j] = 1000
    return c > 0


def checkFlashes(input: np.ndarray):
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            if 10 <= input[i, j] < 1000:
                # when neighbor is > 9, go through entire field again:
                if increaseNeighbors(input, i, j):
                    checkFlashes(input)


def step(input: np.ndarray):
    input += 1
    checkFlashes(input)
    flashes = input > 9
    input[:, :] = input - np.multiply(flashes, input)
    return np.sum(flashes)


def solution_1(input: np.ndarray):
    flashes = 0
    for i in range(100):
        flashes += step(input)
        if (i + 1) % 10 == 0:
            print("Step {}: {} flashes".format(i + 1, flashes))
    return flashes


def solution_2(input: np.ndarray):
    goal: np.ndarray = np.zeros(input.shape)
    i = 0
    while np.any(input != goal):
        step(input)
        i += 1
    return i


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = np.array(parseIntMatrix(input))

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
