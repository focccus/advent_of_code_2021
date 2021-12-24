"""Solution module for Day X, YEAR"""
import copy
import time
import math

from utils.fetch import fetch
from utils.parse import split_str_by_newline


def topElement(burrow: str):
    for i, c in enumerate(burrow):
        if c != ".":
            return c, i + 1
    return None, 0


def burrowCorrect(burrows, i):
    ch = chr(i + ord("A"))
    return all(c == ch or c == "." for c in burrows[i])


def burrowEnterable(moves: range, burrows, pos):
    hallPos = 2 * pos + 2
    return burrowCorrect(burrows, pos) and hallPos in moves


def allPossibleMoves(i, occupied):
    low = i
    high = i
    lDone = hDone = False
    for j in range(1, 10):
        lDone = lDone or (i + j) in occupied
        if not lDone and i + j < 11:
            high = i + j
        hDone = hDone or (i - j) in occupied
        if not hDone and i - j >= 0:
            low = i - j
        if lDone and hDone:
            return range(low, high + 1)
    return range(0, 11)


targetPos = {"A": 0, "B": 1, "C": 2, "D": 3}
possibleMoves = [0, 1] + list(range(3, 9, 2)) + [10]
maxCost = 15950


def moveFromTo(i, m, hall):
    if i != m:
        hall = hall[:m] + hall[i] + hall[m + 1 :]
        hall = hall[:i] + "." + hall[i + 1 :]
    return hall

def step(hall: str, burrows, cost,n=0):
    if burrows == [c * len(burrows[0]) for c in "ABCD"]:
        return cost
    if cost > maxCost or n > 10:
        return math.inf
    occupied = [i for i in range(0, 11) if hall[i] != "."]
    if len(occupied) == 1 and occupied[0] % 2 == 1:
        occupied = []

    mins = [math.inf]

    for i in occupied:
        moves = allPossibleMoves(i, occupied)
        targetB = targetPos[hall[i]]
        costSingle = 10 ** targetB
        if moves and moves != range(i, i + 1):
            if burrowEnterable(moves, burrows, targetB):
                hallPos = 2 * targetB + 2
                costDown = topElement(burrows[targetB])[1] or 0
                return step(
                    hall[:i] + "." + hall[i + 1 :],
                    burrows,
                    cost + (abs(hallPos - i) + costDown) * costSingle,
                    n=n+1
                )
            for m in moves:
                if m in possibleMoves and m != i:
                    mins.append(
                        step(
                            moveFromTo(i, m, hall),
                            burrows,
                            cost + abs(m - i) * costSingle,
                            n=n+1
                        )
                    )
    for b, burrow in enumerate(burrows):
        hallPos = 2 * b + 2
        if not burrowCorrect(burrows, b) and hall[hallPos] == ".":
            top, costU = topElement(burrow)
            if top:
                costSingle = 10 ** targetPos[top]
                mins.append(
                    step(
                        hall[:hallPos] + top + hall[hallPos + 1 :],
                        tuple(
                            list(burrows)[:b]
                            + [burrow.replace(top, ".", 1)]
                            + list(burrows)[b + 1 :]
                        ),
                        cost + costU * costSingle,
                        n=n+1
                    )
                )
    return min(v for v in mins if v)


# min1 = 15299
def solution_1(hall, burrows):
    minCost = step(hall, burrows, 0)
    print(allPossibleMoves(5, [1, 6]))
    return minCost


# min2 = 46453
def solution_2(hall, burrows):
    pass


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    lines = split_str_by_newline(input)
    hall = lines[1][1:-1]
    burrows = tuple("".join([l[i] for l in lines[2:-1]]) for i in [3, 5, 7, 9])

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(hall), copy.deepcopy(burrows))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(hall), copy.deepcopy(burrows))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
