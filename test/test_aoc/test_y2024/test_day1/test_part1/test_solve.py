import pathlib

from aoc.y2024.day1.part1 import solve


def test_parse():
    # Given
    given_input = pathlib.Path(__file__).parent / "test_input"
    expected_output = ((3, 4, 2, 1, 3, 3), (4, 3, 5, 3, 9, 3))
    # When
    output = solve.parse(given_input)
    # Then
    assert output == expected_output


def test_solve():
    # Given
    given_input = pathlib.Path(__file__).parent / "test_input"
    expected_output = 11
    # When
    output = solve.solve(given_input)
    # Then
    assert output == expected_output
