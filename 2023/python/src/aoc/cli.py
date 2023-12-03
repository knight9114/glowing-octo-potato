# -------------------------------------------------------------------------
#   Advent of Code Command-Line Interface
# -------------------------------------------------------------------------

from argparse import ArgumentParser, Namespace
from importlib import import_module
from pathlib import Path


# -------------------------------------------------------------------------
#   CLI Function
# -------------------------------------------------------------------------


def main(argv: tuple[str] | None = None):
    args = parse_cli_args(argv)
    solver = import_module(f"aoc.solvers.d{args.day:02d}")

    if args.part == "1" or args.part == "all":
        print(f"Part #1: {solver.part_1(args.inputs.read_text())}")

    if args.part == "2" or args.part == "all":
        print(f"Part #2: {solver.part_2(args.inputs.read_text())}")


# -------------------------------------------------------------------------
#   Argument Parsing
# -------------------------------------------------------------------------


def parse_cli_args(argv: tuple[str] | None = None) -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("day", type=int)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("--part", choices=["1", "2", "all"], default="all")
    return parser.parse_args(argv)


# -------------------------------------------------------------------------
#   Script Mode
# -------------------------------------------------------------------------

if __name__ == "__main__":
    main()
