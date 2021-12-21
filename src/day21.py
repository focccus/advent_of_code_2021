"""Solution module for Day X, YEAR"""
import functools
import time

from utils.fetch import fetch
from utils.parse import parse_all_numbers

def calcPos(pl: int, rolled: int):
    return (pl - 1 + rolled) % 10 + 1


def game(p1: int, p2: int):
    score1 = score2 = 0
    p1Turn = True
    rolls = 0
    while score1 < 1000 and score2 < 1000:
        val = 3 * (rolls % 100) + 6
        rolls += 3
        if p1Turn:
            p1 = calcPos(p1, val)
            score1 += p1
        else:
            p2 = calcPos(p2, val)
            score2 += p2
        p1Turn = not p1Turn
    return min(score1, score2), rolls


# how often a+b+c appears in all 27 dice possibilities
combinations = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

# cache all previous results
@functools.lru_cache(maxsize=None)
def multiverseGame(p1: int, p2: int, sc1: int, sc2: int, p1Turn: bool):
    if sc1 >= 21:
        return 1, 0
    if sc2 >= 21:
        return 0, 1

    sum1 = sum2 = 0
    for k in combinations:
        if p1Turn:
            p = calcPos(p1, k)
            num1, num2 = multiverseGame(p, p2, sc1 + p, sc2, False)
        else:
            p = calcPos(p2, k)
            num1, num2 = multiverseGame(p1, p, sc1, sc2 + p, True)
        sum1 += combinations[k] * num1
        sum2 += combinations[k] * num2
    return sum1, sum2


def solution_1(player1, player2):
    minScore, rolls = game(player1, player2)
    return minScore * rolls


def solution_2(p1, p2):
    return max(multiverseGame(p1, p2, 0, 0, True))


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_all_numbers(input)

    tic = time.perf_counter()
    s1 = solution_1(parsed_input[1], parsed_input[3])
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input[1], parsed_input[3])
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
