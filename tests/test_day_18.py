import pytest

from aoc2024 import day_18
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_18_1.txt"


@pytest.mark.parametrize(
    "given_start, given_goal, given_dimension, given_corrupted_space, expected_path",
    (
        (
            0 + 0j,
            0 + 2j,
            3 + 3j,
            {0 + 1j, 1 + 1j},
            (1 + 0j, 2 + 0j, 2 + 1j, 2 + 2j, 1 + 2j, 0 + 2j),
        ),
    ),
)
def test_find_shortest_path(
    given_start, given_goal, given_dimension, given_corrupted_space, expected_path
):
    shortest_path = day_18.shortest_path(
        given_start, given_goal, given_dimension, given_corrupted_space
    )
    assert shortest_path == expected_path


def test_parse_input():
    parsed_input = day_18.parse_input(TEST_INPUT_1)

    assert parsed_input
    assert isinstance(parsed_input, tuple)
    assert all(isinstance(item, complex) for item in parsed_input)


def test_solving_part_1_gives_expected_value():
    answer = day_18.solve_part_one(TEST_INPUT_1, dimension=7 + 7j, bytes=12)
    expected_answer = 22
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_18.solve_part_two(TEST_INPUT_1, dimension=7 + 7j)
    expected_answer = (6, 1)
    assert answer == expected_answer
