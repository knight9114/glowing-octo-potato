# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

import re


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    total = 0
    for line in inputs.rstrip("\n").split("\n"):
        digits = [ch for ch in line if ch.isdigit()]
        total += int(digits[0] + digits[-1])

    return total


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    pat = re.compile(f"(?=(\d|{'|'.join(mapping.keys())}))")

    total = 0
    for line in inputs.rstrip("\n").split("\n"):
        digits = [
            m if m.isnumeric() else mapping[m]
            for m in re.findall(pat, line)
        ]
        total += int(digits[0] + digits[-1])

    return total
