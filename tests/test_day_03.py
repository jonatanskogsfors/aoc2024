import pytest

from aoc2024 import day_03
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_3_1.txt"
TEST_INPUT_2 = INPUT_DIR / "test_input_3_2.txt"


@pytest.mark.parametrize(
    "given_instruction, expected_output",
    (("mul(44,46)", 2024),),
)
def test_multiply_match(given_instruction, expected_output):
    match = day_03.MUL_PATTERN.match(given_instruction)
    output = day_03.multiply_match(match)
    assert output == expected_output


def test_solving_part_1_gives_expected_value():
    answer = day_03.solve_part_one(TEST_INPUT_1)
    expected_answer = 161
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_03.solve_part_two(TEST_INPUT_2)
    expected_answer = 48
    assert answer == expected_answer
