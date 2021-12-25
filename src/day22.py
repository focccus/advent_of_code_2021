"""Solution module for Day X, YEAR"""
import copy
import time
import numpy as np

from utils.fetch import fetch
from utils.parse import split_str_by_newline, parse_all_numbers


def cornerPoints(x1, x2, y1, y2, z1, z2):
    return [(x, y, z) for x in [x1, x2] for y in [y1, y2] for z in [z1, z2]]


def isInArea(x, y, z, area):
    (x1, x2, y1, y2, z1, z2) = area
    return x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2


def volume(a):
    return (1 + a[1] - a[0]) * (1 + a[3] - a[2]) * (1 + a[5] - a[4])


def overlap1DIntervals(a1, a2, b1, b2):
    c1 = c2 = 0
    if b1 <= a2 <= b2:
        c1 = max(a1,b1)
        c2 = a2
        a2 = c1 - 1
        b1 = c2 + 1
    elif a1 <= b2 <= a2:
        c1 = max(a1,b1)
        c2 = b2
        b2 = c1 - 1
        a1 = c2 + 1

    return [(a1, a2), (c1, c2), (b1, b2)]


# splits up two cubes into smaller pieces, last piece of second is intersection
def overlap3DIntervals(area1, area2):
    (x11, x12, y11, y12, z11, z12) = area1
    (x21, x22, y21, y22, z21, z22) = area2

    xis = overlap1DIntervals(x11, x12, x21, x22)
    yis = overlap1DIntervals(y11, y12, y21, y22)
    zis = overlap1DIntervals(z11, z12, z21, z22)

    if xis[1] != (0, 0) and yis[1] != (0, 0) and zis[1] != (0, 0):
        res1 = []
        res2 = []
        # x boundary cubes
        if xis[0][0] <= xis[0][1]:
            res1.append((*xis[0], y11, y12, z11, z12))
        if xis[2][0] <= xis[2][1]:
            res2.append((*xis[2], y21, y22, z21, z22))
        # y boundary cubes
        if yis[0][0] <= yis[0][1]:
            res1.append((*xis[1], *yis[0], z11, z12))
        if yis[2][0] <= yis[2][1]:
            res2.append((*xis[1], *yis[2], z21, z22))
        # z boundary cubes
        if zis[0][0] <= zis[0][1]:
            res1.append((*xis[1], *yis[1], *zis[0]))

        if zis[2][0] <= zis[2][1]:
            res2.append((*xis[1], *yis[1], *zis[2]))
        # intersection cube
        res2.append((*xis[1], *yis[1], *zis[1]))
        return res1, res2
    return [area1], [area2]


def overlapArea3D(area1, area2):
    points = []
    for p in cornerPoints(*area1):
        if isInArea(*p, area2):
            points.append(p)
    for p in cornerPoints(*area2):
        if isInArea(*p, area1):
            points.append(p)
    if points == []:
        return None

    x1 = min(points, key=lambda p: p[0])[0]
    x2 = max(points, key=lambda p: p[0])[0]
    y1 = min(points, key=lambda p: p[1])[1]
    y2 = max(points, key=lambda p: p[1])[1]
    z1 = min(points, key=lambda p: p[2])[2]
    z2 = max(points, key=lambda p: p[2])[2]

    return (x1, x2, y1, y2, z1, z2)


def setState(field: np.ndarray, area, state=True, limit=50):
    (x1, x2, y1, y2, z1, z2) = area
    if limit:
        x1 = max(x1, -limit) + limit
        y1 = max(y1, -limit) + limit
        z1 = max(z1, -limit) + limit
        x2 = min(x2, limit) + limit
        y2 = min(y2, limit) + limit
        z2 = min(z2, limit) + limit
        if max(x1, y1, z1) == 0 or min(x2, y2, z2) == 2 * limit:
            return
    field[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = state


def solution_1(input, limit=50):
    size = 2 * limit + 1
    field = np.full((size, size, size), False, dtype=bool)
    for state, area in input:
        setState(field, area, state, limit=limit)
    return np.sum(field)


def translateToMcCommands(cubes,x=0,y=0,z=0):
    blocks = [
        "white",
        "orange",
        "magenta",
        "light_blue",
        "yellow",
        "lime",
        "pink",
        "gray",
        "light_gray",
        "cyan",
        "purple",
        "blue",
        "brown",
        "red",
        "black",
    ]
    return "\n".join(
        [
            f"/fill ~{x1-x} ~{y1-y} ~{z1-z} ~{x2-x} ~{y2-y} ~{z2-z} minecraft:{blocks[i % len(blocks)]}_stained_glass"
            for i, (x1, x2, y1, y2, z1, z2) in enumerate(cubes)
        ]
    )


def solution_2(input):
    on = [input[0][1]]
    for state, area in input[1:]:
        
        oldOn = copy.deepcopy(on)
        on = []
        toAdd = [area]
        for a in oldOn:
            nextCubes = []
            for subA in toAdd:
                a1, a2 = overlap3DIntervals(a, subA)
                on = on + a1
                nextCubes = nextCubes + a2
            toAdd = nextCubes
        if state:
            on = on + toAdd

    return sum(map(volume, on))


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
#     input = """on x=13..13,y=11..13,z=11..13
# off x=9..11,y=9..11,z=9..11"""
    lines = split_str_by_newline(input)
    parsed_input = [(l[:2] == "on", tuple(parse_all_numbers(l[5:]))) for l in lines]
    # print(parsed_input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
