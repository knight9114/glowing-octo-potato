# -------------------------------------------------------------------------
#   Solver
# -------------------------------------------------------------------------

from collections import Counter
from dataclasses import dataclass
from itertools import product
from typing import Self


# -------------------------------------------------------------------------
#   Utilities
# -------------------------------------------------------------------------


CARDS: dict[str, int] = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "j": 1,
}


def hand_type(s: str) -> int:
    hand = Counter(s)
    match len(hand):
        # high card
        case 5:
            return 0

        # one pair
        case 4:
            return 1

        # five of a kind
        case 1:
            return 6

        # four of a kind / full house
        case 2:
            c1, c2 = map(lambda p: p[1], hand.most_common(2))
            if c1 == 4 and c2 == 1:
                return 5

            elif c1 == 3 and c2 == 2:
                return 4

            else:
                raise AssertionError("impossible hand - case 2")

        # three of a kind / two pair
        case 3:
            c1, c2, c3 = map(lambda p: p[1], hand.most_common(3))
            if c1 == 3 and c2 == 1 and c3 == 1:
                return 3

            elif c1 == 2 and c2 == 2 and c3 == 1:
                return 2

            else:
                raise AssertionError("impossible hand - case 3")

        case _:
            raise AssertionError("impossible hand - case ?")


@dataclass
class Hand:
    hand: str
    bid: int
    score: int

    @classmethod
    def from_str(cls, s: str) -> Self:
        hand, bidstr = s.split(maxsplit=1)
        bid = int(bidstr)
        return cls(hand, bid, hand_type(hand))

    def __lt__(self, other: Self) -> bool:
        if self.score < other.score:
            return True

        elif self.score > other.score:
            return False

        for h1, h2 in zip(self.hand, other.hand):
            c1, c2 = CARDS[h1], CARDS[h2]
            if c1 < c2:
                return True

            elif c1 > c2:
                return False


def hand_type_with_jokers(s: str) -> int:
    possible = []
    for card in s:
        if card == "j":
            possible.append(
                ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
            )

        else:
            possible.append([card])

    score = 0
    for hand in product(*possible):
        score = max(score, hand_type(hand))

    return score


@dataclass
class JokerHand(Hand):
    hand: str
    bid: int
    score: int

    @classmethod
    def from_str(cls, s: str) -> Self:
        handstr, bidstr = s.split(maxsplit=1)
        hand = handstr.replace("J", "j")
        bid = int(bidstr)
        return cls(hand, bid, hand_type_with_jokers(hand))


# -------------------------------------------------------------------------
#   Part 1
# -------------------------------------------------------------------------


def part_1(inputs: str) -> int:
    hands = list(Hand.from_str(s) for s in inputs.rstrip("\n").split("\n"))
    ordered = sorted(hands)
    return sum(h.bid * i for i, h in enumerate(ordered, 1))


# -------------------------------------------------------------------------
#   Part 2
# -------------------------------------------------------------------------


def part_2(inputs: str) -> int:
    hands = list(JokerHand.from_str(s) for s in inputs.rstrip("\n").split("\n"))
    ordered = sorted(hands)
    return sum(h.bid * i for i, h in enumerate(ordered, 1))
