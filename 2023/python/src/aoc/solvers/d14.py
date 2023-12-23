# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


def tilt(row: str) -> str:
    output = ""
    n = len(row)
    offset = 0

    while offset != n + 1:
        try:
            block = row.index("#", offset)
        except ValueError:
            block = n

        rolled = row.count("O", offset, block)
        output += "O" * rolled + "." * (block - rolled - offset) + "#"
        offset = block + 1

    return output[:-1]


def tilt_north(rows: list[str]) -> list[str]:
    tilted = map(tilt, map(lambda t: "".join(t), zip(*rows)))
    return list(map(lambda t: "".join(t), zip(*tilted)))


def tilt_south(rows: list[str]) -> list[str]:
    tilted = map(tilt, map(lambda t: "".join(t)[::-1], zip(*rows)))
    return list(map(lambda t: "".join(t), zip(*tilted)))[::-1]


def tilt_west(rows: list[str]) -> list[str]:
    tilted = map(tilt, rows)
    return list(tilted)


def tilt_east(rows: list[str]) -> list[str]:
    tilted = map(tilt, map(lambda t: t[::-1], rows))
    return list(map(lambda t: t[::-1], tilted))


def stitch(rows: list[str]) -> str:
    return "\n".join(rows)


def compute_load(rows: list[str]) -> int:
    n = len(rows)
    load = 0
    for i, row in enumerate(rows):
        load += (n - i) * row.count("O")

    return load


def run_cycle(rows: list[str]) -> list[str]:
    return tilt_east(tilt_south(tilt_west(tilt_north(rows))))


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    rows = inputs.rstrip().split("\n")
    rows = tilt_north(rows)
    return compute_load(rows)


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    rows = inputs.rstrip().split("\n")

    seen = {inputs: 0}
    length = 0
    offset = 0
    for i in range(1, 1000000000):
        rows = run_cycle(rows)
        stitched = stitch(rows)

        if stitched in seen:
            offset = seen[stitched]
            length = i - offset
            break

        else:
            seen[stitched] = i

    diff = (1000000000 - offset) % length
    for i in range(diff):
        rows = run_cycle(rows)

    return compute_load(rows)
