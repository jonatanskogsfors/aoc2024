import pytest

from aoc2024 import day_02
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_02_1.txt"


@pytest.mark.parametrize(
    "given_report, expected_safe",
    (
        ((7, 6, 4, 2, 1), True),
        ((1, 2, 7, 8, 9), False),
        ((1, 3, 2, 4, 5), False),
        ((1, 3, 6, 7, 9), True),
    ),
)
def test_is_safe(given_report, expected_safe):
    assert day_02.is_safe(given_report) == expected_safe


@pytest.mark.parametrize(
    "given_report, expected_safe",
    (
        ((7, 6, 4, 2, 1), True),
        ((1, 2, 7, 8, 9), False),
        ((1, 3, 2, 4, 5), True),
        ((8, 6, 4, 4, 1), True),
    ),
)
def test_is_safe_with_problem_dampener(given_report, expected_safe):
    assert day_02.is_safe(given_report, problem_dampener=True) == expected_safe


def test_parse_input():
    parsed_input = day_02.parse_input(TEST_INPUT_1)

    assert isinstance(parsed_input, tuple)
    expected_input_length = 6
    assert len(parsed_input) == expected_input_length
    assert all(isinstance(report, tuple) for report in parsed_input)


def test_solving_part_1_gives_expected_value():
    answer = day_02.solve_part_one(TEST_INPUT_1)
    expected_answer = 2
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_02.solve_part_two(TEST_INPUT_1)
    expected_answer = 4
    assert answer == expected_answer
