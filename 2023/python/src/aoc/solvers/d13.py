# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

from dataclasses import dataclass
from typing import Self


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


@dataclass
class Map:
    rows: list[int]
    cols: list[int]

    @classmethod
    def from_str(cls, s: str) -> Self:
        ncols = s.index("\n")

        rows = []
        for row in s.rstrip().split("\n"):
            x = 0
            for i, c in enumerate(row[::-1]):
                if c == "#":
                    x ^= 1 << i
            rows.append(x)

        cols = []
        for col in [s[i :: ncols + 1] for i in range(ncols)]:
            x = 0
            for i, c in enumerate(col):
                if c == "#":
                    x ^= 1 << i
            cols.append(x)

        return cls(rows, cols)

    @staticmethod
    def find_reflection(lines: list[int], tolerance: int, target: int) -> int:
        possible = []
        for i, val in enumerate(lines[1:], 1):
            if (val ^ lines[i - 1]).bit_count() <= tolerance:
                possible.append(i)

        for p in possible:
            dist = min(len(lines) - p, p)
            if (
                sum((lines[p + i] ^ lines[p - i - 1]).bit_count() for i in range(dist))
                == target
            ):
                return p

        return 0

    def find_horizontal_reflection(self, tolerance: int, target: int) -> int:
        return self.find_reflection(self.rows, tolerance, target)

    def find_vertical_reflection(self, tolerance: int, target: int) -> int:
        return self.find_reflection(self.cols, tolerance, target)


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    maps = [Map.from_str(s) for s in inputs.rstrip().split("\n\n")]
    horizontal = sum(m.find_horizontal_reflection(0, 0) for m in maps)
    vertical = sum(m.find_vertical_reflection(0, 0) for m in maps)
    return vertical + (100 * horizontal)


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    maps = [Map.from_str(s) for s in inputs.rstrip().split("\n\n")]
    horizontal = sum(m.find_horizontal_reflection(1, 1) for m in maps)
    vertical = sum(m.find_vertical_reflection(1, 1) for m in maps)
    return vertical + (100 * horizontal)
