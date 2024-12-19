import pytest

from aoc2024 import day_19
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_19_1.txt"


@pytest.mark.parametrize(
    "given_stripes, given_design, expected_is_possible",
    (
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "brwrr", True),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "bggr", True),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "gbbr", True),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "rrbgbr", True),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "ubwu", False),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "bwurrg", True),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "brgr", True),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "bbrgwb", False),
    ),
)
def test_is_possible(given_stripes, given_design, expected_is_possible):
    possible = day_19.is_possible(given_design, given_stripes)
    assert possible == expected_is_possible


@pytest.mark.parametrize(
    "given_stripes, given_design, expected_combinations",
    (
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "brwrr", 2),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "bggr", 1),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "gbbr", 4),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "rrbgbr", 6),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "ubwu", 0),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "bwurrg", 1),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "brgr", 2),
        (("r", "wr", "b", "g", "bwu", "rb", "gb", "br"), "bbrgwb", 0),
    ),
)
def test_number_of_combinations(given_stripes, given_design, expected_combinations):
    combinations = day_19.number_of_combinations(given_design, given_stripes)
    assert combinations == expected_combinations


def test_parse_input():
    parsed_input = day_19.parse_input(TEST_INPUT_1)

    assert isinstance(parsed_input, tuple)
    expected_number_of_components = 2
    assert len(parsed_input) == expected_number_of_components
    stripes, designs = parsed_input

    assert stripes
    assert isinstance(stripes, tuple)
    assert all(isinstance(stripe, str) for stripe in stripes)

    assert designs
    assert isinstance(designs, tuple)
    assert all(isinstance(design, str) for design in designs)


def test_solving_part_1_gives_expected_value():
    answer = day_19.solve_part_one(TEST_INPUT_1)
    expected_answer = 6
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_19.solve_part_two(TEST_INPUT_1)
    expected_answer = 16
    assert answer == expected_answer
