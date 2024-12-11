from collections import defaultdict

import pytest

from aoc2024 import day_11
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_11_1.txt"


@pytest.mark.parametrize(
    "given_stones, expected_stones",
    (
        ({0: 1}, {1: 1}),
        ({1: 1}, {2024: 1}),
        ({2024: 1}, {20: 1, 24: 1}),
        ({125: 1, 17: 1}, {253000: 1, 1: 1, 7: 1}),
        ({253000: 1, 1: 1, 7: 1}, {253: 1, 0: 1, 2024: 1, 14168: 1}),
        ({253: 1, 0: 1, 2024: 1, 14168: 1}, {512072: 1, 1: 1, 20: 1, 24: 1, 28676032: 1}),
    ),
)
def test_blink(given_stones, expected_stones):
    stones = defaultdict(int, given_stones)
    day_11.blink(stones)
    stones = {k: v for k, v in stones.items() if v}
    assert stones == expected_stones


def test_parse_input():
    parsed_input = day_11.parse_input(TEST_INPUT_1)
    assert isinstance(parsed_input, defaultdict)

    expected_length = 2
    assert len(parsed_input) == expected_length

    assert all(isinstance(stone, int) for stone in parsed_input.keys())


def test_solving_part_1_gives_expected_value():
    answer = day_11.solve_part_one(TEST_INPUT_1)
    expected_answer = 55312
    assert answer == expected_answer
