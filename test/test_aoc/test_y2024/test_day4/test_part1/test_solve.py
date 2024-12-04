import pathlib

from aoc.y2024.day4.part1 import solve


def test_parse():
    # Given
    given_input = pathlib.Path(__file__).parent / "test_input"
    expected_output = (
        ("M", "M", "M", "S", "X", "X", "M", "A", "S", "M"),
        ("M", "S", "A", "M", "X", "M", "S", "M", "S", "A"),
        ("A", "M", "X", "S", "X", "M", "A", "A", "M", "M"),
        ("M", "S", "A", "M", "A", "S", "M", "S", "M", "X"),
        ("X", "M", "A", "S", "A", "M", "X", "A", "M", "M"),
        ("X", "X", "A", "M", "M", "X", "X", "A", "M", "A"),
        ("S", "M", "S", "M", "S", "A", "S", "X", "S", "S"),
        ("S", "A", "X", "A", "M", "A", "S", "A", "A", "A"),
        ("M", "A", "M", "M", "M", "X", "M", "M", "M", "M"),
        ("M", "X", "M", "X", "A", "X", "M", "A", "S", "X"),
    )

    # When
    output = solve.parse(given_input)
    # Then
    assert output == expected_output


def test_solve():
    # Given
    given_input = pathlib.Path(__file__).parent / "test_input"
    expected_output = 18
    # When
    output = solve.solve(given_input)
    # Then
    assert output == expected_output
