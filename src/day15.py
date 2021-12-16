"""Solution module for Day X, YEAR"""
import copy
import time
import numpy as np

from utils.fetch import fetch
from utils.parse import parseIntMatrix


def neighbors(p):
    (i, j) = p
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


def minPath(i, j, weights: np.ndarray):
    n = weights.shape[0]
    if i == n - 1:
        if j == n - 1:
            return 0
        return minPath(i, j + 1, weights) + weights[i, j]
    if j == n - 1:
        return minPath(i + 1, j, weights) + weights[i, j]

    return min(minPath(i + 1, j, weights), minPath(i, j + 1, weights)) + weights[i, j]


# Djikstra's algorithm
def createDistanceField(weights: np.ndarray):
    n = weights.shape[0]
    visited = np.full((n, n), False, dtype=bool)
    dst = np.ones((n, n)) * np.inf
    dst[0, 0] = 0
    while not np.all(visited):
        u = np.where(~visited & (dst == np.amin(dst + visited * 10000)))
        i = u[0][0]
        j = u[1][0]

        if i < n - 1 and not visited[i + 1, j]:
            dst[i + 1, j] = min(dst[i, j] + weights[i + 1, j], dst[i + 1, j])
        if i > 0 and not visited[i - 1, j]:
            dst[i - 1, j] = min(dst[i, j] + weights[i - 1, j], dst[i - 1, j])
        if j < n - 1 and not visited[i, j + 1]:
            dst[i, j + 1] = min(dst[i, j] + weights[i, j + 1], dst[i, j + 1])
        if j > 0 and not visited[i, j - 1]:
            dst[i, j - 1] = min(dst[i, j] + weights[i, j - 1], dst[i, j - 1])
        visited[i, j] = True
    return dst


def solution_1(input):
    distances = createDistanceField(input)
    print(distances)
    return distances[-1, -1]


def enlargenInput(input) -> np.ndarray:
    n = input.shape[0]
    larger = np.zeros((n * 5, n * 5))
    for i in range(5):
        for j in range(5):
            larger[n * i : n * (i + 1), n * j : n * (j + 1)] = input + i + j
    return np.mod(larger, 10) + 1 * (larger > 9)


def solution_2(input):
    larger = enlargenInput(input)
    distances = createDistanceField(larger)
    return distances[-1, -1]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    #     input = """1163751742
    # 1381373672
    # 2136511328
    # 3694931569
    # 7463417111
    # 1319128137
    # 1359912421
    # 3125421639
    # 1293138521
    # 2311944581"""
    parsed_input = np.array(parseIntMatrix(input))

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
