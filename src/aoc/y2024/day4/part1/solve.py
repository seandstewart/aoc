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
    words: list[tuple[str, ...]] = []
    for y, row in enumerate(board):
        for x, char in enumerate(row):
            if char != WORD[0]:
                continue

            words.extend(iterwords(x=x, y=y, board=board))

    return len(words)


def iterwords(*, x: int, y: int, board: Board) -> t.Iterable[tuple[str, ...]]:
    for one, two, three, four in (
        # Forwards
        ((y, x), (y, x + 1), (y, x + 2), (y, x + 3)),
        # Backwards
        ((y, x), (y, x - 1), (y, x - 2), (y, x - 3)),
        # Upwards
        ((y, x), (y + 1, x), (y + 2, x), (y + 3, x)),
        # Downwards
        ((y, x), (y - 1, x), (y - 2, x), (y - 3, x)),
        # Diagonal up/right
        ((y, x), (y + 1, x + 1), (y + 2, x + 2), (y + 3, x + 3)),
        # Diagonal down/right
        ((y, x), (y - 1, x + 1), (y - 2, x + 2), (y - 3, x + 3)),
        # Diagonal down/left
        ((y, x), (y - 1, x - 1), (y - 2, x - 2), (y - 3, x - 3)),
        # Diagonal up/left
        ((y, x), (y + 1, x - 1), (y + 2, x - 2), (y + 3, x - 3)),
    ):
        # Don't allow overflows
        if any(c[0] < 0 or c[1] < 0 for c in (one, two, three, four)):
            continue

        with contextlib.suppress(IndexError):
            word = (
                board[one[0]][one[1]],
                board[two[0]][two[1]],
                board[three[0]][three[1]],
                board[four[0]][four[1]],
            )
            if word == WORD:
                yield word


type Board = tuple[tuple[str, ...], ...]


WORD = ("X", "M", "A", "S")


if __name__ == "__main__":
    print(solve(INPUT))
