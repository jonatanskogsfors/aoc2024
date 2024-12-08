import pytest

from aoc2024 import day_08
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_08_1.txt"


@pytest.mark.parametrize(
    "given_antenna_positions, given_bound, given_harmonics, expected_antinodes",
    (
        ({4 + 3j, 5 + 5j}, 9 + 9j, False, {3 + 1j, 6 + 7j}),
        ({4 + 3j, 5 + 5j, 8 + 4j}, 9 + 9j, False, {3 + 1j, 6 + 7j, 0 + 2j, 2 + 6j}),
        (
            {0 + 0j, 1 + 2j, 3 + 1j},
            9 + 9j,
            True,
            {0 + 0j, 1 + 2j, 2 + 4j, 3 + 1j, 3 + 6j, 4 + 8j, 5 + 0j, 6 + 2j, 9 + 3j},
        ),
    ),
)
def test_antinodes_for_antennas(
    given_antenna_positions, given_bound, given_harmonics, expected_antinodes
):
    antinodes = day_08.antinodes_for_antennas(
        given_antenna_positions, given_bound, given_harmonics
    )
    assert antinodes == expected_antinodes


def test_parse_input():
    parsed_input = day_08.parse_input(TEST_INPUT_1)

    expected_input_length = 2
    assert len(parsed_input) == expected_input_length
    antennas, bound = parsed_input

    assert isinstance(antennas, dict)
    assert isinstance(bound, complex)

    expected_antenna_frequencies = 2
    assert len(antennas) == expected_antenna_frequencies


def test_solving_part_1_gives_expected_value():
    answer = day_08.solve_part_one(TEST_INPUT_1)
    expected_answer = 14
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_08.solve_part_two(TEST_INPUT_1)
    expected_answer = 34
    assert answer == expected_answer
