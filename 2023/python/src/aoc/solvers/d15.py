# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

from functools import reduce
from operator import add


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


def ascii_hash(s: str) -> int:
    return reduce(lambda acc, x: ((acc + ord(x)) * 17) % 256, s, 0)


def hashmap(acc: list[dict[str, int]], instruction: str) -> list[dict[str, int]]:
    op = "-" if "-" in instruction else "="
    label, op, operand = instruction.partition(op)

    hidx = ascii_hash(label)
    box = acc[hidx]
    lens = int(operand) if operand else None

    if op == "-" and lens is None and box.get(label) is not None:
        box.pop(label)

    elif op == "=" and lens is not None:
        box[label] = lens

    return acc


def enum_add(x: int, args: tuple[int, int]) -> int:
    return x + (args[0] * args[1])


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    return reduce(add, map(ascii_hash, inputs.rstrip().split(",")))


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    boxes = reduce(hashmap, inputs.rstrip().split(","), [{} for _ in range(256)])
    powers = map(
        lambda box: reduce(enum_add, enumerate(box.values(), 1), 0),
        boxes,
    )
    return reduce(enum_add, enumerate(powers, 1), 0)
