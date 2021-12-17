"""Solution module for Day X, YEAR"""
import copy
import time
from functools import reduce
from operator import mul

from utils.fetch import fetch


class Packet:
    def __init__(self, source: str):
        self.source = source
        self.version = int(source[:3], 2)
        self.typeId = int(source[3:6], 2)
        self.subpackets = []
        self.readHead = 0

        if self.typeId == 4:
            self.readLiteral()
        else:
            self.readOperator()

    def readLiteral(self):
        num = ""
        i = 6
        while self.source[i] == "1":
            num += self.source[i + 1 : i + 5]
            i += 5
        num += self.source[i + 1 : i + 5]
        self.readHead = i + 5
        self.literal = int(num, 2)

    def readOperator(self):
        self.lengthType = self.source[6]
        if self.lengthType == "0":
            # Gives length of all subpackets
            totalL = int(self.source[7:22], 2)
            newSource = self.source[22 : 22 + totalL]
            self.readHead = 22
            while newSource != "":
                sp = Packet(newSource)
                newSource = newSource[sp.readHead :]
                self.readHead += sp.readHead
                self.subpackets.append(sp)

        else:
            # Gives number of subpackets
            numPacks = int(self.source[7:18], 2)
            newSource = self.source[18:]
            self.readHead = 18
            for _ in range(numPacks):
                sp = Packet(newSource)
                newSource = newSource[sp.readHead :]
                self.readHead += sp.readHead
                self.subpackets.append(sp)

    def computeVersionSum(self):
        return self.version + sum(sp.computeVersionSum() for sp in self.subpackets)

    def eval(self):
        if self.typeId == 4:
            return self.literal
        subp = [sp.eval() for sp in self.subpackets]
        if self.typeId == 0:
            return sum(subp)
        if self.typeId == 1:
            return reduce(mul, subp, 1)
        if self.typeId == 2:
            return min(subp)
        if self.typeId == 3:
            return max(subp)
        if self.typeId == 5:
            return 1 if subp[0] > subp[1] else 0
        if self.typeId == 6:
            return 1 if subp[0] < subp[1] else 0
        if self.typeId == 7:
            return 1 if subp[0] == subp[1] else 0


def solution_1(input):
    binary = bin(int(input, 16))[2:].zfill(len(input) * 4)
    p = Packet(binary)
    return p.computeVersionSum()


def solution_2(input):
    binary = bin(int(input, 16))[2:].zfill(len(input) * 4)
    p = Packet(binary)
    return p.eval()


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
