import pytest

from aoc2024 import day_04
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_4_1.txt"


@pytest.mark.parametrize(
    "given_word_search, expected_x_positions",
    (
        ((), set()),
        (("X",), {(0, 0)}),
        ((".X.", "X.X", "..X"), {(1, 0), (0, 1), (2, 1), (2, 2)}),
    ),
)
def test_get_x_positions(given_word_search, expected_x_positions):
    x_positions = day_04.get_x_positions(given_word_search)
    assert x_positions == expected_x_positions


@pytest.mark.parametrize(
    "given_x_position, expected_mas_candidates",
    (
        (
            (5, 5),
            {
                frozenset(((6, 5), (7, 5), (8, 5))),
                frozenset(((4, 5), (3, 5), (2, 5))),
                frozenset(((5, 6), (5, 7), (5, 8))),
                frozenset(((5, 4), (5, 3), (5, 2))),
                frozenset(((6, 6), (7, 7), (8, 8))),
                frozenset(((4, 4), (3, 3), (2, 2))),
                frozenset(((6, 4), (7, 3), (8, 2))),
                frozenset(((4, 6), (3, 7), (2, 8))),
            },
        ),
    ),
)
def test_get_mas_candidates(given_x_position, expected_mas_candidates):
    mas_candidates = day_04.mas_candidates(given_x_position)
    assert mas_candidates == expected_mas_candidates

@pytest.mark.parametrize(
    "given_wordsearch, given_mas_candidate, expected_mas",
    (
        (("MAS",), set(((0, 0), (1, 0), (2, 0))), True),
        (("MAS",), set(((2, 0), (1, 0), (0, 0))), False),
    )
)
def test_is_mas(given_wordsearch, given_mas_candidate, expected_mas):
    mas = day_04.is_mas(given_wordsearch, given_mas_candidate)
    assert mas == expected_mas

def test_solving_part_1_gives_expected_value():
    pass
    # answer = day_04.solve_part_one(TEST_INPUT_1)
    # expected_answer = 18
    # assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    pass
    # answer = day_04.solve_part_two(TEST_INPUT_1)
    # expected_answer = 48
    # assert answer == expected_answer
