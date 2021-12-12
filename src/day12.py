"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_str_by_newline


def findAllPaths(neighbors, start: str, end: str, visited, maxLowerVisitCount=1):
    if start == end:
        return [[end]]
    paths = []
    for dir in neighbors[start]:
        c = visited.count(dir)
        if dir.isupper() or c < maxLowerVisitCount:
            newCount = maxLowerVisitCount
            if dir.islower() and c + 1 == maxLowerVisitCount == 2:
                newCount -= 1
            paths.extend(
                findAllPaths(neighbors, dir, end, visited + [start], newCount,)
            )
    for p in paths:
        p.insert(0, start)
    return paths


def printPaths(paths):
    for p in paths:
        print("-".join(p))


def buildNeighborTable(tuples):
    nb = {}
    for (start, end) in tuples:
        if start in nb:
            nb[start].append(end)
        else:
            nb[start] = [end]
        if end in nb:
            nb[end].append(start)
        else:
            nb[end] = [start]
    return nb


def solution(neighbors, maxLowerVisitCount=1):
    paths = findAllPaths(
        neighbors, "start", "end", ["start", "start"], maxLowerVisitCount
    )
    return len(paths)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [tuple(l.split("-")) for l in split_str_by_newline(input)]
    neighbors = buildNeighborTable(parsed_input)

    tic = time.perf_counter()
    s1 = solution(copy.deepcopy(neighbors))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution(copy.deepcopy(neighbors), 2)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
