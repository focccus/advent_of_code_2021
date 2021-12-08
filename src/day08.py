"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import split_str_by_newline, split_str_by_separator


def parseSegmentLine(l: str):
    return [
        "".join(sorted(seg)) for seg in split_str_by_separator(l, " ") if seg != "|"
    ]


def solution_1(input):
    return len([d for line in input for d in line[10:] if len(d) in [2, 3, 4, 7]])


def segment_diff(seg1: str, seg2: str):
    return "".join([c for c in seg1 if not c in seg2])


def countCharacters(digits, count="abcdefg"):
    return [(c, sum(c in seg for seg in digits)) for c in count]


def findCharacterByDistribution(charMap, distr=1):
    return next(c for (c, i) in charMap if i == distr)


def line_sol(line):
    signals, outputs = line[:10], line[10:]

    signals.sort(key=len)
    print(signals)

    translate = {
        signals[0]: 1,
        signals[1]: 7,
        signals[2]: 4,
        signals[9]: 8,
    }
    len5 = signals[3:6]
    len6 = signals[6:9]
    print(len5, len6)
    # A does only once appear in 1 or 7!
    A = findCharacterByDistribution(
        countCharacters([signals[0], signals[1]], signals[1]), 1
    )
    # B does only once appear in 2,3,5 when only looking at segments from 4
    B = findCharacterByDistribution(countCharacters(len5, signals[2]), 1)
    five = next(seg for seg in len5 if B in seg)
    len5.remove(five)
    translate[five] = 5
    # F must be the one when counting characters wrt 5
    F = findCharacterByDistribution(countCharacters([signals[0]], five), 1)
    C = next(c for c in signals[0] if c != F)
    # 3 is now the only one with F
    three = next(seg for seg in len5 if F in seg)
    len5.remove(three)
    translate[three] = 3
    # last one must be 2
    translate[len5[0]] = 2
    print(translate)

    # 6 is only one not having C
    six = next(seg for seg in len6 if not C in seg)
    translate[six] = 6
    len6.remove(six)

    D = findCharacterByDistribution(countCharacters(signals, signals[2]), 7)
    # 0 is only one not having D
    print(D)
    zero = next(seg for seg in len6 if not D in seg)
    print(zero)
    translate[zero] = 0
    len6.remove(zero)
    print(zero)

    # last one is 9
    translate[len6[0]] = 9
    print(translate)

    return int("".join([str(translate[o]) for o in outputs]))


def solution_2(input):
    return sum(map(line_sol, input))


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
#     input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    parsed_input = [parseSegmentLine(l) for l in split_str_by_newline(input)]

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")


# a: 8
# b: 6
# c: 8
# d: 7
# e: 4
# f: 9
# g: 7

