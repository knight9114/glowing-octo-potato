# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

import math


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    timeline, distline = inputs.rstrip("\n").split("\n", 1)
    times = list(map(int, timeline.split(":", 1)[1].split()))
    dists = list(map(int, distline.split(":", 1)[1].split()))

    margins = 1
    for t, d in zip(times, dists):
        func = lambda x: -(x**2) + t * x - d
        lower = math.ceil((t - math.sqrt(t**2 - 4 * d)) / 2)
        upper = math.floor((t + math.sqrt(t**2 - 4 * d)) / 2)

        if func(lower) == 0:
            lower += 1

        if func(upper) == 0:
            upper -= 1

        margins *= upper - lower + 1

    return margins


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    timeline, distline = inputs.rstrip("\n").split("\n", 1)
    t = int("".join(timeline.split(":", 1)[1].split()))
    d = int("".join(distline.split(":", 1)[1].split()))

    margins = 1
    func = lambda x: -(x**2) + t * x - d
    lower = math.ceil((t - math.sqrt(t**2 - 4 * d)) / 2)
    upper = math.floor((t + math.sqrt(t**2 - 4 * d)) / 2)

    if func(lower) == 0:
        lower += 1

    if func(upper) == 0:
        upper -= 1

    margins *= upper - lower + 1

    return margins
