"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_str_by_newline


def printDots(dots):
    maxRows = max(dots, key=lambda x: x[1])[1]
    maxCols = max(dots, key=lambda x: x[0])[0]
    for i in range(maxRows + 1):
        print(" ".join(["#" if (j, i) in dots else "." for j in range(maxCols + 1)]))
    print("\n")


def fold(dots, line, foldHorizontal=False):
    newdots = []
    for d in dots:
        replaceFirst = foldHorizontal and d[0] > line
        replaceSecond = not foldHorizontal and d[1] > line
        d = (
            d[0] - replaceFirst * 2 * (d[0] - line),
            d[1] - replaceSecond * 2 * (d[1] - line),
        )
        if not d in newdots:
            newdots.append(d)
    return newdots


def solution_1(dots, folds):
    dots = fold(dots, folds[0][1], folds[0][0] == "x")
    return len(dots)


def solution_2(dots, folds):
    for f in folds:
        dots = fold(dots, f[1], f[0] == "x")
    printDots(dots)
    return len(dots)


def parseFoldLine(l):
    assign = l.split(" ")[2].split("=")
    return (assign[0], int(assign[1]))


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    split = input.split("\n\n")
    dots = [
        (int(l.split(",")[0]), int(l.split(",")[1]))
        for l in split_str_by_newline(split[0])
    ]
    folds = [parseFoldLine(l) for l in split_str_by_newline(split[1])]

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(dots), folds)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(dots), folds)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
