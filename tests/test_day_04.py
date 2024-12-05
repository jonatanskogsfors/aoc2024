import pytest

from aoc2024 import day_04
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_04_1.txt"
TEST_INPUT_2 = INPUT_DIR / "test_input_04_2.txt"


@pytest.mark.parametrize(
    "given_word_search, given_letter, expected_x_positions",
    (
        ((), "X", set()),
        ((), "A", set()),
        (("X",), "X", {(0, 0)}),
        ((".X.", "X.X", "..X"), "X", {(1, 0), (0, 1), (2, 1), (2, 2)}),
        (("AX.", "X.X", ".AX"), "A", {(0, 0), (1, 2)}),
    ),
)
def test_get_x_positions(given_word_search, given_letter, expected_x_positions):
    x_positions = day_04.get_positions(given_word_search, letter=given_letter)
    assert x_positions == expected_x_positions


@pytest.mark.parametrize(
    "given_x_position, expected_mas_candidates",
    (
        (
            (5, 5),
            {
                ((6, 5), (7, 5), (8, 5)),
                ((5, 6), (5, 7), (5, 8)),
                ((5, 4), (5, 3), (5, 2)),
                ((6, 6), (7, 7), (8, 8)),
                ((4, 4), (3, 3), (2, 2)),
                ((4, 5), (3, 5), (2, 5)),
                ((6, 4), (7, 3), (8, 2)),
                ((4, 6), (3, 7), (2, 8)),
            },
        ),
    ),
)
def test_get_mas_candidates(given_x_position, expected_mas_candidates):
    mas_candidates = day_04.mas_candidates(given_x_position)
    assert mas_candidates == expected_mas_candidates


@pytest.mark.parametrize(
    "given_a_position, expected_x_mas_candidates",
    (
        (
            (5, 5),
            {
                ((4, 4), (6, 6)),
                ((6, 6), (4, 4)),
                ((6, 4), (4, 6)),
                ((4, 6), (6, 4)),
            },
        ),
    ),
)
def test_get_x_mas_candidates(given_a_position, expected_x_mas_candidates):
    x_mas_candidates = day_04.x_mas_candidates(given_a_position)
    assert x_mas_candidates == expected_x_mas_candidates


@pytest.mark.parametrize(
    "given_wordsearch, given_mas_candidate, expected_mas",
    (
        (("MAS",), ((0, 0), (1, 0), (2, 0)), True),
        (("MAS",), ((2, 0), (1, 0), (0, 0)), False),
        (("M",), ((-1, -1), (0, 0), (1, 1)), False),
    ),
)
def test_is_mas(given_wordsearch, given_mas_candidate, expected_mas):
    mas = day_04.is_mas(given_wordsearch, given_mas_candidate)
    assert mas == expected_mas


@pytest.mark.parametrize(
    "given_wordsearch, given_x_mas_candidate, expected_x_mas",
    (
        (("M..", "...", "..S"), ((0, 0), (2, 2)), True),
        (("..S", "...", "M.."), ((0, 2), (2, 0)), True),
        (("S..", "...", "..M"), ((0, 0), (2, 1)), False),
    ),
)
def test_is_x_mas(given_wordsearch, given_x_mas_candidate, expected_x_mas):
    x_mas = day_04.is_x_mas(given_wordsearch, given_x_mas_candidate)
    assert x_mas == expected_x_mas


def test_parse_input():
    parsed_input = day_04.parse_input(TEST_INPUT_1)
    assert isinstance(parsed_input, tuple)

    expected_height = 10
    assert len(parsed_input) == expected_height

    expected_width = 10
    assert all(
        isinstance(row, str) and len(row) == expected_width for row in parsed_input
    )


def test_solving_part_1_gives_expected_value():
    answer = day_04.solve_part_one(TEST_INPUT_1)
    expected_answer = 18
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_04.solve_part_two(TEST_INPUT_2)
    expected_answer = 9
    assert answer == expected_answer
