# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

from functools import reduce


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


def compute_diffs(row: list[int]) -> list[list[int]]:
    diffs = [row.copy()]
    while not all(i == 0 for i in diffs[-1]):
        newdiff = [right - left for left, right in zip(diffs[-1], diffs[-1][1:])]
        diffs.append(newdiff)

    return diffs


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    readings = [
        list(map(int, line.split())) for line in inputs.rstrip("\n").split("\n")
    ]

    total = 0
    for row in readings:
        diffs = compute_diffs(row)
        total += reduce(lambda x, y: y[-1] + x, diffs[::-1], 0)

    return total


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    readings = [
        list(map(int, line.split())) for line in inputs.rstrip("\n").split("\n")
    ]

    total = 0
    for row in readings:
        diffs = compute_diffs(row)
        total += reduce(lambda x, y: y[0] - x, diffs[::-1], 0)

    return total
