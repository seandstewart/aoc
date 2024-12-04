#!/usr/bin/env python
from __future__ import annotations

import contextlib
import pathlib
import typing as t

INPUT = pathlib.Path(__file__).parent / "input"


def parse(pth: pathlib.Path) -> Board:
    return tuple(tuple(r) for r in pth.read_text().splitlines())


def solve(pth: pathlib.Path):
    board = parse(pth)
    words: list[tuple[tuple[str, ...], ...]] = []
    for y, row in enumerate(board):
        for x, char in enumerate(row):
            if char != WORD[0][1]:
                continue

            words.extend(iterwords(x=x, y=y, board=board))

    return len(words)


def iterwords(
    *, x: int, y: int, board: Board
) -> t.Iterable[tuple[tuple[str, ...], ...]]:
    for (fone, ftwo, fthree), (sone, stwo, sthree) in (
        # Forwards
        (
            ((y + 1, x - 1), (y, x), (y - 1, x + 1)),
            ((y - 1, x - 1), (y, x), (y + 1, x + 1)),
        ),
        # Forwards Inverse
        (
            ((y + 1, x - 1), (y, x), (y - 1, x + 1)),
            ((y + 1, x + 1), (y, x), (y - 1, x - 1)),
        ),
        # Backwards
        (
            ((y + 1, x + 1), (y, x), (y - 1, x - 1)),
            ((y - 1, x + 1), (y, x), (y + 1, x - 1)),
        ),
        # Backwards Inverse
        (
            ((y - 1, x + 1), (y, x), (y + 1, x - 1)),
            ((y - 1, x - 1), (y, x), (y + 1, x + 1)),
        ),
    ):
        # Don't allow overflows
        if any(c[0] < 0 or c[1] < 0 for c in (fone, ftwo, fthree, sone, stwo, sthree)):
            continue

        with contextlib.suppress(IndexError):
            first = (
                board[fone[0]][fone[1]],
                board[ftwo[0]][ftwo[1]],
                board[fthree[0]][fthree[1]],
            )
            second = (
                board[sone[0]][sone[1]],
                board[stwo[0]][stwo[1]],
                board[sthree[0]][sthree[1]],
            )
            if (first, second) == WORD:
                yield first, second


type Board = tuple[tuple[str, ...], ...]


WORD = (("M", "A", "S"), ("M", "A", "S"))


if __name__ == "__main__":
    print(solve(INPUT))
