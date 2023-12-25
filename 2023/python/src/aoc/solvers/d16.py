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

    def __add__(self, rhs: Self) -> Self:
        return Point(self.r + rhs.r, self.c + rhs.c)

    @classmethod
    def direction(cls, direction: str) -> Self:
        match direction:
            case ">":
                return cls(0, 1)

            case "<":
                return cls(0, -1)

            case "^":
                return cls(-1, 0)

            case "v":
                return cls(1, 0)

            case _:
                raise ValueError(f"invalid {direction=}")


@dataclass(frozen=True)
class Beam:
    p: Point
    d: str

    @classmethod
    def default(cls) -> Self:
        return cls(Point(0, 0), ">")

    def step(self, space: str, seen: set[Self], bound: Point) -> list[Self]:
        output = []

        # null space
        if (
            space == "."
            or (space == "-" and self.d in ("<", ">"))
            or (space == "|" and self.d in ("^", "v"))
        ):
            output.append(Beam(self.p + Point.direction(self.d), self.d))

        # reflect
        elif space in ("/", "\\"):
            d: str = NotImplemented
            match (space, self.d):
                case ("/", "^") | ("\\", "v"):
                    d = ">"

                case ("/", "v") | ("\\", "^"):
                    d = "<"

                case ("/", ">") | ("\\", "<"):
                    d = "^"

                case ("/", "<") | ("\\", ">"):
                    d = "v"

            output.append(Beam(self.p + Point.direction(d), d))

        # split
        elif space == "-" and self.d in ("^", "v"):
            output.extend(
                [
                    Beam(self.p + Point.direction("<"), "<"),
                    Beam(self.p + Point.direction(">"), ">"),
                ]
            )

        elif space == "|" and self.d in ("<", ">"):
            output.extend(
                [
                    Beam(self.p + Point.direction("^"), "^"),
                    Beam(self.p + Point.direction("v"), "v"),
                ]
            )

        return list(
            filter(
                lambda p: p not in seen
                and 0 <= p.p.r < bound.r
                and 0 <= p.p.c < bound.c,
                output,
            )
        )


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    rows = inputs.rstrip().split("\n")
    cave: dict[Point, str] = {
        Point(r, c): s for r, row in enumerate(rows) for c, s in enumerate(row)
    }
    bound = Point(len(rows), len(rows[0]))
    seen: set[Beam] = set()

    heads = [Beam.default()]
    while heads:
        update = []
        for head in heads:
            seen.add(head)
            update.extend(head.step(cave[head.p], seen, bound))
        heads = update

    return len(set([b.p for b in seen]))


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    rows = inputs.rstrip().split("\n")
    cave: dict[Point, str] = {
        Point(r, c): s for r, row in enumerate(rows) for c, s in enumerate(row)
    }
    bound = Point(len(rows), len(rows[0]))

    energized = 0
    starting_points = [
        *[Beam(Point(0, i), "v") for i in range(bound.c)],
        *[Beam(Point(bound.r - 1, i), "^") for i in range(bound.c)],
        *[Beam(Point(i, 0), ">") for i in range(bound.r)],
        *[Beam(Point(i, bound.c - 1), "<") for i in range(bound.r)],
    ]

    for start in starting_points:
        seen: set[Beam] = set()
        heads = [start]
        while heads:
            update = []
            for head in heads:
                seen.add(head)
                update.extend(head.step(cave[head.p], seen, bound))
            heads = update

        energized = max(energized, len(set([b.p for b in seen])))

    return energized
