"""Solution module for Day X, YEAR"""
import copy
import time
import string

from utils.fetch import fetch
from utils.parse import split_double_newline_pair, split_str_by_newline


# old inefficient
def polymerStep(template: str, rules):
    newtemp = template[0]
    for t in template[1:]:
        newtemp += rules[newtemp[-1] + t] + t
    return newtemp


def solutionDumb(template: str, rules, iterations=10):
    for _ in range(iterations):
        template = polymerStep(template, rules)
    counts = [c for char in string.ascii_uppercase if (c := template.count(char)) > 0]
    return max(counts) - min(counts)


def solution(template: str, rules, iterations=10):
    pairs = [c1 + c2 for (c1, c2) in zip(template, template[1:])]
    counts = {p: pairs.count(p) for p in pairs}
    for _ in range(iterations):
        for k, v in counts.copy().items():
            ins = rules[k]
            counts[k[0] + ins] = counts.get(k[0] + ins, 0) + v
            counts[ins + k[1]] = counts.get(ins + k[1], 0) + v
            counts[k] -= v
    # Transfer to count of starting letters
    alphaCount = [
        sum(counts.get(c + C, 0) for C in string.ascii_uppercase)
        for c in string.ascii_uppercase
    ]
    # Add last letter which is missing before
    alphaCount[ord(template[-1]) - ord("A")] += 1
    # Filter non-zero
    alphaCount = [n for n in alphaCount if n]
    return max(alphaCount) - min(alphaCount)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    template, input_rules = split_double_newline_pair(input)
    rules = {}
    for l in split_str_by_newline(input_rules):
        rules[l[:2]] = l[6:7]

    tic = time.perf_counter()
    s1 = solution(template, copy.deepcopy(rules))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution(template, copy.deepcopy(rules), 40)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
