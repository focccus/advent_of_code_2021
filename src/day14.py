"""Solution module for Day X, YEAR"""
import copy
import time
import string
import numpy as np

from utils.fetch import fetch
from utils.parse import split_double_newline_pair, split_str_by_newline


def countLetters(pair, rules, depth) -> np.ndarray:
    if depth == 0:
        return np.zeros(26)
    l = rules[pair]
    counts = countLetters(pair[0] + l, rules, depth - 1)
    counts = counts + countLetters(l + pair[1], rules, depth - 1)
    counts[ord(pair[0]) - 65] += 1
    counts[ord(pair[1]) - 65] += 1

    return counts


# old inefficient
def polymerStep(template: str, rules):
    newtemp = template[0]
    for t in template[1:]:
        newtemp += rules[newtemp[-1] + t] + t
    return newtemp


def solution(template: str, rules, iterations=10):
    for _ in range(iterations):
        template = polymerStep(template, rules)
    counts = [c for char in string.ascii_uppercase if (c := template.count(char)) > 0]
    return max(counts) - min(counts)


def solution_2(template: str, rules):
    pairs = [c1 + c2 for (c1, c2) in zip(template, template[1:])]
    print(pairs)
    count = np.zeros(26)
    for p in pairs:
        count += countLetters(p, rules, 9)
    print(count)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    template, input_rules = split_double_newline_pair(input)
    rules = {}
    for l in split_str_by_newline(input_rules):
        rules[l[:2]] = l[6:7]
    print(rules)

    tic = time.perf_counter()
    s1 = solution(template, copy.deepcopy(rules))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution(template, copy.deepcopy(rules),40)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
