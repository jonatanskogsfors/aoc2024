import pytest

from aoc2024 import day_01
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_1_1.txt"


def test_parse_input_to_two_tuples():
    # When parsing input
    parsed_input = day_01.parse_input(TEST_INPUT_1)

    # Then the input is two tuples:
    expected_length = 2
    assert len(parsed_input) == expected_length
    a, b = parsed_input
    assert isinstance(a, tuple)
    assert isinstance(b, tuple)


def test_get_pairs_in_order():
    left, right = day_01.parse_input(TEST_INPUT_1)

    last_a = None
    last_b = None
    for a, b in day_01.ordered_pairs(left, right):
        assert last_a is None or a >= last_a
        assert last_b is None or b >= last_b
        last_a = a
        last_b = b


def test_get_distance_between_ordered_pairs():
    left, right = day_01.parse_input(TEST_INPUT_1)
    distances = tuple(day_01.distances(left, right))

    assert distances == (2, 1, 0, 1, 2, 5)


@pytest.mark.parametrize(
    "number, list, expected_similarity",
    (
        (3, (4, 3, 5, 3, 9, 3), 9),
        (4, (4, 3, 5, 3, 9, 3), 4),
        (2, (4, 3, 5, 3, 9, 3), 0),
        (1, (4, 3, 5, 3, 9, 3), 0),
    ),
)
def test_similarity_score(number, list, expected_similarity):
    similarity = day_01.similarity(number, list)
    assert similarity == expected_similarity


def test_solving_part_1_gives_expected_value():
    answer = day_01.solve_part_one(TEST_INPUT_1)
    expected_answer = 11
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_01.solve_part_two(TEST_INPUT_1)
    expected_answer = 31
    assert answer == expected_answer
