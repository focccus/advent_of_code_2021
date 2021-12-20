"""Solution module for Day X, YEAR"""
import copy
import time
import numpy as np

from utils.fetch import fetch
from utils.parse import split_str_by_newline


def expandImg(img: np.ndarray, n=1, usingOnes=False):
    fill = 1 if usingOnes else 0
    new = np.full((img.shape[0] + 2 * n, img.shape[1] + 2 * n), fill, dtype=int)
    new[n:-n, n:-n] = img
    return new


def neighborBits(img: np.ndarray, i, j):
    return "".join(str(b) for b in img[i - 1 : i + 2, j - 1 : j + 2].flatten())


def solution(alg, img, iterations=2):
    ozzilateOuter = alg[0] == 1

    for n in range(iterations):
        padWithOnes = n % 2 == 1
        old = expandImg(img, 2, ozzilateOuter and padWithOnes)

        fillNew = 0 if not ozzilateOuter or padWithOnes else 1
        img = np.full(old.shape, fillNew, dtype=int)
        for i in range(1, old.shape[0] - 1):
            for j in range(1, old.shape[1] - 1):
                val = int(neighborBits(old, i, j), 2)
                img[i, j] = alg[val]

    return np.sum(img == 1)


def parse01Line(l):
    return [1 if c == "#" else 0 for c in l]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    lines = split_str_by_newline(input)
    alg = parse01Line(lines[0])
    img = np.array([parse01Line(l) for l in lines[1:]], dtype=int)
    tic = time.perf_counter()
    s1 = solution(alg, copy.deepcopy(img))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    # Takes a few minutes :D
    tic = time.perf_counter()
    s2 = solution(alg, copy.deepcopy(img), 50)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
