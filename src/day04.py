"""Solution module for Day X, YEAR"""
import copy
import time

from utils.fetch import fetch
from utils.parse import (
    parse_matrix,
    split_str_by_separator,
    parse_all_numbers,
)


def mark_and_check(board, number):
    row = col = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if number == 16:
                print(i, j, board[i][j])
            if board[i][j] == number:
                row = i
                col = j

                board[i][j] = -1

                break
    # check row
    if [-1] * 5 == board[row]:
        return True
    res = True
    # check col
    for i in range(0, 5):
        res = res and board[i][col] == -1
    return res


def solution_1(input, boards):

    for num in input:
        for board in boards:
            if mark_and_check(board, num):
                return sum([item for row in board for item in row if item >= 0]) * num


def solution_2(input, boards):
    for num in input:
        for board in boards:

            if len(boards) == 1:
                print(num)
                mark_and_check(board, num)

                print(board)

                return sum([item for row in board for item in row if item >= 0]) * num
            print(num)
            if mark_and_check(board, num):
                boards.remove(board)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    split = input.split("\n", 1)
    parsed_input = parse_all_numbers(split[0])

    boards = list(map(parse_matrix, split[1].split("\n\n")))

    tic = time.perf_counter()
    s1 = solution_1(parsed_input, copy.deepcopy(boards))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input, copy.deepcopy(boards))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
