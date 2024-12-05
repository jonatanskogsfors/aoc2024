import pytest

from aoc2024 import day_{{ '{:02}'.format(day) }}
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_{{ '{:02}'.format(day) }}_1.txt"


def test_parse_input():
    parsed_input = day_{{ '{:02}'.format(day) }}.parse_input(TEST_INPUT_1)


def test_solving_part_1_gives_expected_value():
    answer = day_{{ '{:02}'.format(day) }}.solve_part_one(TEST_INPUT_1)
    # expected_answer =
    # assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_{{ '{:02}'.format(day) }}.solve_part_two(TEST_INPUT_1)
    # expected_answer =
    # assert answer == expected_answer
