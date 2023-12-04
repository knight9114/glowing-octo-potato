# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

import re


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    regame = re.compile("Card\s+\d+: ")
    resplit = re.compile(" [|] |\n")
    inputs = re.sub(regame, "", inputs)
    splits = [line for line in re.split(resplit, inputs) if line != ""]
    assert len(splits) % 2 == 0

    winning = list(map(lambda line: [int(d) for d in line.split()], splits[0::2]))
    scratches = list(map(lambda line: [int(d) for d in line.split()], splits[1::2]))

    total = 0
    for winners, scratched in zip(winning, scratches):
        value = 0
        for scratch in scratched:
            if scratch in winners:
                value = value * 2 if value else 1

        total += value

    return total


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    regame = re.compile("Card\s+\d+: ")
    resplit = re.compile(" [|] |\n")
    inputs = re.sub(regame, "", inputs)
    splits = [line for line in re.split(resplit, inputs) if line != ""]
    assert len(splits) % 2 == 0

    winning = list(map(lambda line: [int(d) for d in line.split()], splits[0::2]))
    scratches = list(map(lambda line: [int(d) for d in line.split()], splits[1::2]))

    multipliers = [1 for _ in range(len(winning))]
    for i, (winners, scratched) in enumerate(zip(winning, scratches)):
        repeats = sum(1 for s in scratched if s in winners)
        if repeats > 0:
            for j in range(repeats):
                multipliers[i + j + 1] += multipliers[i]

    return sum(multipliers)
