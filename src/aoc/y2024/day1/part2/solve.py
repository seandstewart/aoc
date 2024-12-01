#!/usr/bin/env python
from __future__ import annotations

import collections
import collections.abc as c
import csv
import pathlib

INPUT = pathlib.Path(__file__).parent / "input"


def parse(pth: pathlib.Path) -> tuple[c.Iterable[int], c.Iterable[int]]:
    text = pth.read_text().strip().replace("   ", ",")
    reader = csv.reader(text.splitlines(), delimiter=",")
    left, right = zip(*((int(lft), int(rht)) for lft, rht in reader))
    return left, right


def solve(pth: pathlib.Path) -> int:
    left, right = parse(pth)
    counts = collections.Counter(right)
    return sum((lft * counts[lft] for lft in left))


if __name__ == "__main__":
    print(solve(INPUT))
