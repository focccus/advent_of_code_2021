"""Solution module for Day X, YEAR"""
import copy
import time
import json

from utils.fetch import fetch
from utils.parse import split_str_by_newline

printSteps = False


class Tree:
    def __init__(self, l=None, r=None, parent=None):
        self.parent = parent
        self.depth = 0
        self.l = l
        self.r = r

    def fromArray(self, input):
        if type(input) == int:
            self.val = input
        else:
            self.l = Tree(parent=self).fromArray(input[0])
            self.r = Tree(parent=self).fromArray(input[1])
            self.depth = max(self.l.depth, self.r.depth) + 1
        return self

    def toArray(self):
        if self.l and self.r:
            return [self.l.toArray(), self.r.toArray()]
        return self.val

    def magnitude(self) -> int:
        if self.l and self.r:
            return 3 * self.l.magnitude() + 2 * self.r.magnitude()
        return self.val

    def increaseLeftMost(self, amount):
        if self.l:
            self.l.increaseLeftMost(amount)
        else:
            self.val += amount

    def increaseRightMost(self, amount):
        if self.r:
            self.r.increaseRightMost(amount)
        else:
            self.val += amount

    def explode(self, n=0):
        if n < 3:
            if self.l and self.r:
                side, toAdd = self.l.explode(n + 1)
                if side > 0:
                    self.r.increaseLeftMost(toAdd)
                    return side, 0
                if side < 0:
                    return side, toAdd

                side, toAdd = self.r.explode(n + 1)
                if side < 0:
                    self.l.increaseRightMost(toAdd)
                    return side, 0
                if side > 0:
                    return side, toAdd
        elif self.l and self.r:
            side = 0
            toAdd = 0
            if self.l.l and self.l.r:
                toAdd = self.l.l.val
                side = -1
                addR = self.l.r.val
                self.l = Tree(parent=self).fromArray(0)
                self.r.increaseLeftMost(addR)
            elif self.r.r and self.r.l:
                toAdd = self.r.r.val
                side = 1
                addL = self.r.l.val
                self.r = Tree(parent=self).fromArray(0)
                self.l.increaseRightMost(addL)
            self.updateDepthUp()
            return side, toAdd
        return 0, 0

    def split(self):
        if self.l and self.r:
            if self.l.split() or self.r.split():
                # self.depth = max(self.l.depth, self.r.depth) + 1
                return True
        elif self.val >= 10:
            half = self.val // 2
            self.l = Tree(parent=self).fromArray(half)
            self.r = Tree(parent=self).fromArray(
                half if self.val % 2 == 0 else half + 1
            )
            self.updateDepthUp()
            del self.val
            return True

    def updateDepthUp(self):
        if self.l and self.r:
            self.depth = max(self.l.depth, self.r.depth) + 1
        if self.parent:
            self.parent.updateDepthUp()

    def add(self, other):
        t = Tree(self, other)
        self.parent = t
        other.parent = t
        t.depth = max(self.depth, other.depth) + 1

        return t.reduce()

    def reduce(self):
        didSplit = True
        while didSplit:
            while self.depth > 4:
                self.explode()
                if printSteps:
                    print("explode", self.toArray())
            didSplit = self.split()
            if printSteps and didSplit:
                print("split  ", self.toArray())
        return self


def snailfishSum(numbers):
    current = numbers[0]
    for n in numbers[1:]:
        current = current.add(n)
        if printSteps:
            print(current.toArray())
    return current


def solution_1(input):
    trees = [Tree().fromArray(l) for l in input]
    sum = snailfishSum(trees)
    return sum.magnitude()


def solution_2(input):
    trees = [Tree().fromArray(l) for l in input]

    maxMag = 0
    for t in trees:
        for tree in trees:
            if tree == t:
                continue
            t2 = copy.deepcopy(t)
            tree2 = copy.deepcopy(tree)
            maxMag = max(maxMag, t2.add(tree2).magnitude())
    return maxMag


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [json.loads(l) for l in split_str_by_newline(input)]

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
