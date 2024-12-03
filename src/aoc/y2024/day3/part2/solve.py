#!/usr/bin/env python
from __future__ import annotations

import pathlib
import re
import typing as t

INPUT = pathlib.Path(__file__).parent / "input"


def parse(pth: pathlib.Path) -> t.Iterable[Mul | Operation]:
    text = pth.read_text().strip()
    for match in re.finditer(PATTERN, text):
        if (instruction := match.group("instruction")) == "mul":
            yield Mul(
                instruction=instruction,
                left=int(match.group("left")),
                right=int(match.group("right")),
            )
            continue

        yield Operation(
            instruction=match.group("instruction"),
        )


class Operation(t.TypedDict):
    instruction: str


class Mul(Operation):
    left: int
    right: int


PATTERN = re.compile(
    r"(?P<instruction>(mul|don't|do))\(((?P<left>\d{1,3}),(?P<right>\d{1,3}))?\)"
)


def solve(pth: pathlib.Path) -> int:
    total = 0
    enabled = True
    for operation in parse(pth):
        if operation["instruction"] == "don't":
            enabled = False
            continue
        if operation["instruction"] == "do":
            enabled = True
            continue
        if not enabled:
            continue

        mul = t.cast(Mul, operation)
        total += mul["left"] * mul["right"]

    return total


if __name__ == "__main__":
    print(solve(INPUT))
