#!/usr/bin/env python
from __future__ import annotations

import collections.abc as c
import csv
import itertools
import operator
import pathlib

INPUT = pathlib.Path(__file__).parent / "input"


def parse(pth: pathlib.Path) -> c.Iterable[c.Iterable[int]]:
    with pth.open("r", newline="") as fp:
        reader = csv.reader(fp, delimiter=" ")
        for row in reader:
            yield tuple(map(int, row))


def solve(pth: pathlib.Path) -> int:
    return sum(issafe(row) for row in parse(pth))


def issafe(row: c.Iterable[int]) -> bool:
    first = next(itertools.pairwise(row))
    op = operator.gt if first[0] > first[1] else operator.lt
    safe = all(op(a, b) and 0 < abs(a - b) < 4 for a, b in itertools.pairwise(row))
    return safe


if __name__ == "__main__":
    print(solve(INPUT))
