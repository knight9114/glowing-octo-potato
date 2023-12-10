# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

from dataclasses import dataclass
from typing import Self


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------

@dataclass(frozen=True)
class Point:
    r: int
    c: int
    s: str


@dataclass(frozen=True)
class Graph:
    nodes: dict[Point, list[Point]]
    nrows: int
    ncols: int
    start: Point

    @classmethod
    def from_str(cls, s: str) -> Self:
        rows = s.rstrip().split("\n")
        nrows = len(rows)
        ncols = len(rows[0])

        g = {}
        start: Point = NotImplemented
        for r, row in enumerate(rows):
            for c, s in enumerate(row):
                p = Point(r, c, s)
                if s == "S":
                    start = p

                neighbors = []

                # north
                if r != 0 and s in "|LJS" and rows[r - 1][c] in "|7FS":
                    neighbors.append(Point(r - 1, c, rows[r - 1][c]))

                # south
                if r != nrows - 1 and s in "|7FS" and rows[r + 1][c] in "|LJS":
                    neighbors.append(Point(r + 1, c, rows[r + 1][c]))

                # west
                if c != 0 and s in "-J7S" and rows[r][c - 1] in "-LFS":
                    neighbors.append(Point(r, c - 1, rows[r][c - 1]))

                # east
                if c != ncols - 1 and s in "-LFS" and rows[r][c + 1] in "-J7S":
                    neighbors.append(Point(r, c + 1, rows[r][c + 1]))

                g[p] = neighbors

        return cls(g, nrows, ncols, start)

    def find_loop(self) -> list[Point]:
        path = [self.start, self.nodes[self.start][0]]
        while path[-1] != self.start:
            neighbors = self.nodes[path[-1]]
            nextnode = neighbors[neighbors.index(path[-2]) ^ 1]
            path.append(nextnode)

        return path[:-1]

    def count_interior_points(self) -> int:
        total = 0
        loop = {(p.r, p.c) : p.s for p in self.find_loop()}

        for p in self.nodes:
            if (p.r, p.c) not in loop:
                count = 0
                for rr, rc in zip(range(p.r + 1, self.nrows), range(p.c + 1, self.ncols)):
                    if loop.get((rr, rc), ".") in "-|FJS":
                        count += 1

                if count % 2 == 1:
                    total += 1

        return total


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    g = Graph.from_str(inputs)
    dist = len(g.find_loop())
    return (dist // 2) + (dist % 2)


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    g = Graph.from_str(inputs)
    return g.count_interior_points()
