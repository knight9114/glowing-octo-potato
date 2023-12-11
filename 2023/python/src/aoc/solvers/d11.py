# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

from dataclasses import dataclass
import itertools
from typing import Self


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


@dataclass(frozen=True)
class Node:
    coords: tuple[int, int]
    distance: int

    def __lt__(self, other: Self) -> bool:
        return self.distance < other.distance


@dataclass(frozen=True)
class Map:
    galaxies: list[tuple[int, int]]
    expansions: tuple[list[int], list[int]]
    nrows: int
    ncols: int

    @classmethod
    def from_str(cls, s: str) -> Self:
        rows = s.rstrip().split("\n")
        nrows = len(rows)
        ncols = len(rows[0])

        g = []
        allrows = [False for _ in range(nrows)]
        allcols = [False for _ in range(ncols)]
        for r, row in enumerate(rows):
            for c, sym in enumerate(row):
                if sym == "#":
                    allrows[r] = True
                    allcols[c] = True
                    g.append((r, c))

        expansions = (
            [i for i, v in enumerate(allrows) if not v],
            [i for i, v in enumerate(allcols) if not v],
        )

        return cls(g, expansions, nrows, ncols)

    def all_shortest_distances(self, expand: int = 1) -> dict[tuple[int, int], int]:
        dists = {}
        for isrc, idst in itertools.combinations(range(len(self.galaxies)), 2):
            dist = 0
            src, dst = self.galaxies[isrc], self.galaxies[idst]
            for r in range(min(src[0], dst[0]), max(src[0], dst[0])):
                dist += 1
                if r in self.expansions[0]:
                    dist += expand

            for c in range(min(src[1], dst[1]), max(src[1], dst[1])):
                dist += 1
                if c in self.expansions[1]:
                    dist += expand

            dists[(src, dst)] = dist

        return dists


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    g = Map.from_str(inputs)
    dists = g.all_shortest_distances()
    return sum(dists.values())


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    g = Map.from_str(inputs)
    dists = g.all_shortest_distances(999999)
    return sum(dists.values())
