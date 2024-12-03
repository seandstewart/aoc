#!/usr/bin/env python
from __future__ import annotations

import pathlib
import re
import typing as t

INPUT = pathlib.Path(__file__).parent / "input"


def parse(pth: pathlib.Path) -> t.Iterable[Operation]:
    text = pth.read_text().strip()
    for match in re.finditer(PATTERN, text):
        yield Operation(
            instruction=match.group("instruction"),
            left=int(match.group("left")),
            right=int(match.group("right")),
        )


class Operation(t.TypedDict):
    instruction: str
    left: int
    right: int


PATTERN = re.compile(r"(?P<instruction>mul+)\((?P<left>\d{1,3}),(?P<right>\d{1,3})\)")


def solve(pth: pathlib.Path) -> int:
    return sum(op["left"] * op["right"] for op in parse(pth))


if __name__ == "__main__":
    print(solve(INPUT))
