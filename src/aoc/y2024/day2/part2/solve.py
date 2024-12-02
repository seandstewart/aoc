#!/usr/bin/env python
from __future__ import annotations

import collections.abc as c
import csv
import itertools
import operator
import pathlib

INPUT = pathlib.Path(__file__).parent / "input"


def parse(pth: pathlib.Path) -> c.Iterable[c.Sequence[int]]:
    with pth.open("r", newline="") as fp:
        reader = csv.reader(fp, delimiter=" ")
        for row in reader:
            yield (*map(int, row),)


def solve(pth: pathlib.Path) -> int:
    return sum(issafe(row) for row in parse(pth))


def issafe(row: c.Sequence[int]) -> bool:
    safe = _issafe_inner(row)
    if safe:
        return safe

    for ix in range(len(row)):
        dampened = (
            *row[0:ix],
            *row[(ix + 1) :],
        )
        safe = _issafe_inner(dampened)
        if safe:
            break
    return safe


def _issafe_inner(row: c.Sequence[int]) -> bool:
    op = operator.gt if row[0] > row[1] else operator.lt
    return all(op(a, b) and 0 < abs(a - b) < 4 for a, b in itertools.pairwise(row))


if __name__ == "__main__":
    print(solve(INPUT))
