#!/usr/bin/env python
from __future__ import annotations

import pathlib

INPUT = pathlib.Path(__file__).parent / "input"


def parse(pth: pathlib.Path): ...


def solve(pth: pathlib.Path): ...


if __name__ == "__main__":
    print(solve(INPUT))
