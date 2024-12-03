import pathlib

from aoc.y2024.day3.part2 import solve


def test_parse():
    # Given
    given_input = pathlib.Path(__file__).parent / "test_input"
    expected_output = [
        solve.Operation(
            instruction="mul",
            left=2,
            right=4,
        ),
        solve.Operation(
            instruction="mul",
            left=5,
            right=5,
        ),
        solve.Operation(
            instruction="mul",
            left=11,
            right=8,
        ),
        solve.Operation(
            instruction="mul",
            left=8,
            right=5,
        ),
    ]
    # When
    output = [*solve.parse(given_input)]
    # Then
    assert output == expected_output


def test_solve():
    # Given
    given_input = pathlib.Path(__file__).parent / "test_input"
    expected_output = 161
    # When
    output = solve.solve(given_input)
    # Then
    assert output == expected_output
