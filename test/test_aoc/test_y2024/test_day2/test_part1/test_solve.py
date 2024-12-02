import pathlib

from aoc.y2024.day2.part1 import solve


def test_parse():
    # Given
    given_input = pathlib.Path(__file__).parent / "test_input"
    expected_output = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    # When
    output = [[*row] for row in solve.parse(given_input)]
    # Then
    assert output == expected_output


def test_solve():
    # Given
    given_input = pathlib.Path(__file__).parent / "test_input"
    expected_output = 2
    # When
    output = solve.solve(given_input)
    # Then
    assert output == expected_output
