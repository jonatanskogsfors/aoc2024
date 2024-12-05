import pytest

from aoc2024 import day_05
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_5_1.txt"


def test_parse_input():
    pair = 2

    parsed_input = day_05.parse_input(TEST_INPUT_1)
    assert len(parsed_input) == pair

    rules, updates = parsed_input

    expected_number_of_rules = 21
    assert len(rules) == expected_number_of_rules
    assert isinstance(rules, set)
    assert all(
        isinstance(rule, tuple)
        and len(rule) == pair
        and all(isinstance(number, int) for number in rule)
        for rule in rules
    )

    expected_number_of_updates = 6
    assert len(updates) == expected_number_of_updates
    assert isinstance(updates, tuple)
    assert all(
        isinstance(update, tuple) and all(isinstance(number, int) for number in update)
        for update in updates
    )


@pytest.mark.parametrize(
    "given_input_path, given_update, expected_in_order",
    (
        (TEST_INPUT_1, (75, 47, 61, 53, 29), True),
        (TEST_INPUT_1, (75, 97, 47, 61, 53), False),
    ),
)
def test_is_in_order(given_input_path, given_update, expected_in_order):
    rules, _ = day_05.parse_input(given_input_path)
    in_order = day_05.is_in_order(rules, given_update)
    assert in_order == expected_in_order


@pytest.mark.parametrize(
    "given_update, expected_middle",
    (
        ((75, 47, 61, 53, 29), 61),
        ((97, 61, 53, 29, 13), 53),
        ((75, 29, 13), 29),
    ),
)
def test_get_middle_page(given_update, expected_middle):
    middle_page = day_05.get_middle_page(given_update)
    assert middle_page == expected_middle


@pytest.mark.parametrize(
    "given_input_path, given_update, expected_update",
    (
        (TEST_INPUT_1, (75, 97, 47, 61, 53), (97, 75, 47, 61, 53)),
        (TEST_INPUT_1, (61, 13, 29), (61, 29, 13)),
        (TEST_INPUT_1, (97, 13, 75, 29, 47), (97, 75, 47, 29, 13)),
    ),
)
def test_fix_update(given_input_path, given_update, expected_update):
    rules, _ = day_05.parse_input(given_input_path)
    updated_update = day_05.fix_update(rules, given_update)
    assert updated_update == expected_update


def test_solving_part_1_gives_expected_value():
    answer = day_05.solve_part_one(TEST_INPUT_1)
    expected_answer = 143
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_05.solve_part_two(TEST_INPUT_1)
    expected_answer = 123
    assert answer == expected_answer
