import pytest

from aoc2024 import day_13
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_13_1.txt"


@pytest.mark.parametrize(
    "given_button_a, given_button_b, given_prize, expected_tokens",
    ((94 + 34j, 22 + 67j, 8400 + 5400j, 280),),
)
def test_calculate_presses(given_button_a, given_button_b, given_prize, expected_tokens):
    tokens = day_13.tokens_for_prize(given_button_a, given_button_b, given_prize)
    assert tokens == expected_tokens


@pytest.mark.parametrize(
    "given_button_1, given_button_2, given_prize, expected_solution",
    (
        (94 + 34j, 22 + 67j, 8400 + 5400j, (80, 40)),
        (26 + 66j, 67 + 21j, 12748 + 12176j, None),
        (17 + 86j, 84 + 37j, 7870 + 6450j, (38, 86)),
        (69 + 23j, 27 + 71j, 18641 + 10279j, None),
    ),
)
def test_a_solution(given_button_1, given_button_2, given_prize, expected_solution):
    solution = day_13.find_solution(given_button_1, given_button_2, given_prize)
    assert solution == expected_solution


@pytest.mark.parametrize(
    "given_equation_1, given_equation_2, expected_solution",
    (
        ((94, 22, 8400), (34, 67, 5400), (80, 40)),
        ((26, 67, 12748), (66, 21, 12176), None),
    ),
)
def test_solve_equation_system(given_equation_1, given_equation_2, expected_solution):
    solution = day_13.solve_equation_system(given_equation_1, given_equation_2)
    assert solution == expected_solution


def test_parse_input():
    parsed_input = day_13.parse_input(TEST_INPUT_1)

    assert parsed_input
    assert isinstance(parsed_input, tuple)
    expected_number_of_components = 3
    assert all(
        isinstance(row, tuple) and len(row) == expected_number_of_components
        for row in parsed_input
    )
    assert all(isinstance(element, complex) for row in parsed_input for element in row)


def test_solving_part_1_gives_expected_value():
    answer = day_13.solve_part_one(TEST_INPUT_1)
    expected_answer = 480
    assert answer == expected_answer
