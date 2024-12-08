from typing import Sequence

import pytest

from aoc2024 import day_07
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_07_1.txt"


@pytest.mark.parametrize(
    "given_operands, given_result, expected_status",
    (
        ((10, 19), 190, True),
        ((81, 40, 27), 3267, True),
        ((11, 6, 16, 20), 292, True),
        ((17, 5), 83, False),
    ),
)
def test_has_solution(
    given_operands: Sequence[int],
    given_result: int,
    expected_status: bool,
):
    status = day_07.has_solution(given_operands, given_result)
    assert status == expected_status


@pytest.mark.parametrize(
    "given_operands, given_result, expected_status",
    (((15, 6), 156, True), ((6, 8, 6, 15), 7290, True), ((17, 8, 14), 192, True)),
)
def test_has_concatenation_solution(
    given_operands: Sequence[int],
    given_result: int,
    expected_status: bool,
):
    status = day_07.has_solution(given_operands, given_result, allowed_operators="+*|")
    assert status == expected_status


def test_parse_input():
    parsed_input = day_07.parse_input(TEST_INPUT_1)

    assert isinstance(parsed_input, tuple)
    expected_length = 9
    assert len(parsed_input) == expected_length

    a_pair = 2
    assert all(len(row) == a_pair for row in parsed_input)
    assert all(
        isinstance(result, int) and isinstance(operands, tuple)
        for result, operands in parsed_input
    )


def test_solving_part_1_gives_expected_value():
    answer = day_07.solve_part_one(TEST_INPUT_1)
    expected_answer = 3749
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_07.solve_part_two(TEST_INPUT_1)
    expected_answer = 11387
    assert answer == expected_answer
