# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

from dataclasses import dataclass
from typing import Self


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


@dataclass
class Game:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __le__(self, other: Self) -> bool:
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )

    @classmethod
    def from_str(cls, s: str) -> Self:
        groups = s.split(", ")
        kwargs = {
            color: int(number) for number, color in map(lambda g: g.split(" "), groups)
        }
        return cls(**kwargs)

    @classmethod
    def from_games(cls, *games: Self) -> Self:
        return cls(
            red=max(g.red for g in games),
            green=max(g.green for g in games),
            blue=max(g.blue for g in games),
        )

    def power(self) -> int:
        return self.red * self.green * self.blue


def parse_inputs(inputs: str) -> list[list[Game]]:
    output = []
    for line in inputs.rstrip("\n").split("\n"):
        _, rounds = line.split(": ", 1)
        output.append([Game.from_str(r) for r in rounds.split("; ")])

    return output


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    compare = Game(red=12, green=13, blue=14)
    total = 0
    for i, row in enumerate(parse_inputs(inputs), 1):
        if all(g <= compare for g in row):
            total += i

    return total


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    total = 0
    for row in parse_inputs(inputs):
        total += Game.from_games(*row).power()
    return total
