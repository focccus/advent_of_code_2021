"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_number_by_separator


# gives how many fish there are initially at day0, day1...
def init_fish(input):
    res = [0] * 9
    for f in input:
        res[f] += 1
    return res


def simulate_day(fish):
    givingBirth = fish[0]
    # swapp to previous
    for i in range(1, 9):
        fish[i - 1] = fish[i]
    # return to day 7
    fish[6] += givingBirth
    # add new fish at day 9
    fish[8] = givingBirth

def solution(input, days = 80):
    fish = init_fish(input)
    for _ in range(days):
        simulate_day(fish)
    return sum(fish)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    # input = "3,4,3,1,2"
    parsed_input = split_number_by_separator(input, ",")

    tic = time.perf_counter()
    s1 = solution(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution(copy.deepcopy(parsed_input),256)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
