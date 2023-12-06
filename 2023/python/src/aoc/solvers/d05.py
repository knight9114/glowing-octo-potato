# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


def parse_rawmaps(chunk) -> list[tuple[int, int, int]]:
    lines = chunk.rstrip().split("\n")[1:]
    output = []

    for line in lines:
        dst, src, n = map(int, line.split())
        output.append((src, src + n - 1, src - dst))

    return sorted(output, key=lambda x: x[0])


def minimal_cover(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges = sorted(ranges, key=lambda x: x[0])

    if len(ranges) == 0:
        return []

    stack = [ranges[0]]

    for rng in ranges[1:]:
        if stack[-1][0] <= rng[0] <= stack[-1][1]:
            stack[-1] = (stack[-1][0], max(stack[-1][1], rng[1]))

        else:
            stack.append(rng)

    return stack


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    rawseeds, *rawmaps = inputs.rstrip("\n").split("\n\n")
    seeds = [s for s in map(int, rawseeds.split(":", 1)[1].split())]
    maps = [parse_rawmaps(r) for r in rawmaps]

    output = 1 << 64
    for seed in seeds:
        update = seed
        for tuples in maps:
            for lower, upper, shift in tuples:
                if lower <= update <= upper:
                    update -= shift
                    break

        output = min(output, update)

    return output


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    rawranges, *rawmaps = inputs.rstrip("\n").split("\n\n")
    rawseeds = [s for s in map(int, rawranges.split(":", 1)[1].split())]
    ranges = minimal_cover(
        [(s, s + n - 1) for s, n in zip(rawseeds[::2], rawseeds[1::2])]
    )
    maps = [parse_rawmaps(r) for r in rawmaps]

    output = 1 << 64
    for seedrange in ranges:
        covers = [seedrange]
        for layermaps in maps:
            update = []
            for start, end in covers:
                current_start = start
                convert = []
                for lower, upper, shift in layermaps:
                    if current_start < lower:
                        convert.append((current_start, lower - 1))
                        current_start = lower

                    if lower <= current_start and current_start <= upper:
                        rangeend = upper if not end <= upper else end
                        convert.append((current_start - shift, rangeend - shift))
                        current_start = rangeend + 1

                    if current_start - 1 == end:
                        break

                if current_start < end:
                    convert.append((current_start, end))

                convert = sorted(convert, key=lambda x: x[0])
                update.append(convert)

            update = [item for sublist in update for item in sublist]
            update = sorted(update, key=lambda x: x[0])
            covers = minimal_cover(update)

        output = min(output, covers[0][0])

    return output
