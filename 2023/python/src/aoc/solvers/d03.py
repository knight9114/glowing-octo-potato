# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

import re


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    lines = inputs.rstrip("\n").split("\n")
    renums = re.compile("(\d+)")
    resyms = re.compile("[^.\d]")
    n = len(lines)

    total = 0
    for i, row in enumerate(lines):
        for mnumber in renums.finditer(row):
            start, end = mnumber.start(), mnumber.end()
            s, e = max(0, start - 1), min(end, n - 1)
            search = (
                "" if i == 0 else lines[i - 1][s : e + 1],
                "" if i == n - 1 else lines[i + 1][s : e + 1],
                row[s],
                row[e],
            )
            if resyms.search("".join(search)):
                total += int(mnumber.group())

    return total


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    lines = inputs.rstrip("\n").split("\n")
    regears = re.compile("[*]")
    renums = re.compile("(\d+)")
    n = len(lines)

    total = 0
    for i, row in enumerate(lines):
        for mgear in regears.finditer(row):
            offset = mgear.span()[0]
            left, right = offset - 1, offset + 1

            adjacent = []
            searches = (
                "" if i == 0 else lines[i - 1],
                row,
                "" if i == n - 1 else lines[i + 1],
            )
            for search in searches:
                for mnum in renums.finditer(search):
                    span = mnum.span()

                    # Handles single-digit numbers
                    if span[1] - span[0] == 1 and span[0] in range(left, right):
                        adjacent.append(int(mnum.group()))

                    # Handles multi-digit numbers
                    elif left in range(*span) or right in range(*span):
                        adjacent.append(int(mnum.group()))

            if len(adjacent) == 2:
                total += adjacent[0] * adjacent[1]

    return total
