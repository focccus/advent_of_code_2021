"""Solution module for Day X, YEAR"""
import copy
import time
import numpy as np

from utils.fetch import fetch
from utils.parse import split_str_by_newline


def getAllRelativeDst(points):
    dst = []
    for p in points:
        s = set()
        for p2 in points:
            if (p != p2).all():
                s.add(tuple(p2 - p))
        dst.append(s)
    return dst


def findSameDsts(dst1, dst2, minSame=12):
    for i, dSet in enumerate(dst1):
        for j, d in enumerate(dst2):
            countSame = 1
            for tup in d:
                if tup in dSet:
                    countSame += 1
                if countSame >= minSame:
                    return i, j
    return None, None


def findPointOf(sc1, sc2, dst1, dst2, minSame=12):
    i, j = findSameDsts(dst1, dst2, minSame)
    if i != None and j != None:
        return sc1[i] - sc2[j]
    return 0 * sc1[0]


def rotations(scanner):
    rots = [[] for _ in range(24)]
    for coord in scanner:
        # positive x
        rots[0].append(np.array([+coord[0], +coord[1], +coord[2]]))
        rots[1].append(np.array([+coord[0], -coord[2], +coord[1]]))
        rots[2].append(np.array([+coord[0], -coord[1], -coord[2]]))
        rots[3].append(np.array([+coord[0], +coord[2], -coord[1]]))
        # negative x
        rots[4].append(np.array([-coord[0], -coord[1], +coord[2]]))
        rots[5].append(np.array([-coord[0], +coord[2], +coord[1]]))
        rots[6].append(np.array([-coord[0], +coord[1], -coord[2]]))
        rots[7].append(np.array([-coord[0], -coord[2], -coord[1]]))
        # positive y
        rots[8].append(np.array([+coord[1], +coord[2], +coord[0]]))
        rots[9].append(np.array([+coord[1], -coord[0], +coord[2]]))
        rots[10].append(np.array([+coord[1], -coord[2], -coord[0]]))
        rots[11].append(np.array([+coord[1], +coord[0], -coord[2]]))
        # negative y
        rots[12].append(np.array([-coord[1], -coord[2], +coord[0]]))
        rots[13].append(np.array([-coord[1], +coord[0], +coord[2]]))
        rots[14].append(np.array([-coord[1], +coord[2], -coord[0]]))
        rots[15].append(np.array([-coord[1], -coord[0], -coord[2]]))
        # positive z
        rots[16].append(np.array([+coord[2], +coord[0], +coord[1]]))
        rots[17].append(np.array([+coord[2], -coord[1], +coord[0]]))
        rots[18].append(np.array([+coord[2], -coord[0], -coord[1]]))
        rots[19].append(np.array([+coord[2], +coord[1], -coord[0]]))
        # negative z
        rots[20].append(np.array([-coord[2], -coord[0], +coord[1]]))
        rots[21].append(np.array([-coord[2], +coord[1], +coord[0]]))
        rots[22].append(np.array([-coord[2], +coord[0], -coord[1]]))
        rots[23].append(np.array([-coord[2], -coord[1], -coord[0]]))
    return rots


def maxTaxicap(points):
    maxDst = 0
    for p1 in points:
        for p2 in points:
            maxDst = max(maxDst, np.sum(np.abs(p2 - p1)))
    return maxDst


def solution(input):
    foundTuples = list(map(tuple, input[0]))
    found = copy.deepcopy(input[0])
    dst = getAllRelativeDst(found)
    toProcess = list(range(1, len(input)))
    scanners = [input[0][0] * 0]

    while len(toProcess) > 0:
        for i in toProcess:
            for rot in rotations(input[i]):
                rel = getAllRelativeDst(rot)
                p = findPointOf(found, rot, dst, rel)
                if np.all(p != 0):
                    print(i, p)
                    scanners.append(p)
                    for beacon in rot:
                        beacon += p
                        if not tuple(beacon) in foundTuples:
                            found.append(beacon)
                            foundTuples.append(tuple(beacon))

                    dst = getAllRelativeDst(found)
                    toProcess.remove(i)
                    break
    print(foundTuples)
    return len(found), maxTaxicap(scanners)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [
        [
            np.fromstring(l, dtype=int, sep=",")
            for l in split_str_by_newline(scanner)[1:]
        ]
        for scanner in input.split("\n\n")
    ]

    tic = time.perf_counter()
    s1, s2 = solution(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
