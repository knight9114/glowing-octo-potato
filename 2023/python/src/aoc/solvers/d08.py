# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

from functools import reduce
from math import gcd
from typing import Callable


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


def parse_coordinates(s: str) -> dict[str, tuple[str, str]]:
    mapping = {}
    for line in s.split("\n"):
        node, rest = line.split(" = ", 1)
        left, right = rest[1:-1].split(", ", 1)
        mapping[node] = (left, right)

    return mapping


def walk(
    node: str,
    leftright: str,
    check: Callable[[str], bool],
    mapping: dict[str, tuple[str, str]],
) -> int:
    n = len(leftright)
    i = 0
    while not check(node):
        next_node = mapping[node][0 if leftright[i % n] == "L" else 1]
        i += 1
        node = next_node

    return i


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    rls, coordblock = inputs.rstrip("\n").split("\n\n")
    mapping = parse_coordinates(coordblock)

    return walk("AAA", rls, lambda n: n == "ZZZ", mapping)


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    rls, coordblock = inputs.rstrip("\n").split("\n\n")
    mapping = parse_coordinates(coordblock)

    starting_points = [
        walk(node, rls, lambda n: n[-1] == "Z", mapping)
        for node in mapping
        if node[-1] == "A"
    ]

    return reduce(
        lambda x, y: abs(x * y) // gcd(x, y),
        starting_points,
    )
