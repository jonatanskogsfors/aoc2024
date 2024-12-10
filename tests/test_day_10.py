import pytest

from aoc2024 import day_10
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_10_1.txt"


@pytest.mark.parametrize(
    "given_map, expected_trailheads",
    (
        (("0", {(0, 0)})),
        (
            (
                "101",
                "010",
                "101",
            ),
            {(1, 0), (0, 1), (2, 1), (1, 2)},
        ),
    ),
)
def test_find_trailheads(given_map, expected_trailheads):
    trailheads = day_10.find_trailheads(given_map)
    assert trailheads == expected_trailheads


@pytest.mark.parametrize(
    "given_map, given_position, expected_paths",
    (
        (
            (
                "202",
                "213",
                "222",
            ),
            (1, 1),
            {(0, 1), (1, 2)},
        ),
    ),
)
def test_find_paths(given_map, given_position, expected_paths):
    paths = day_10.find_paths(given_position, given_map)
    assert paths == expected_paths


@pytest.mark.parametrize(
    "given_map, given_trailhead, expected_score",
    (
        (
            (
                "...0...",
                "...1...",
                "...2...",
                "6543456",
                "7.....7",
                "8.....8",
                "9.....9",
            ),
            (3, 0),
            2,
        ),
        (
            (
                "..90..9",
                "...1.98",
                "...2..7",
                "6543456",
                "765.987",
                "876....",
                "987....",
            ),
            (3, 0),
            4,
        ),
        (
            (
                "10..9..",
                "2...8..",
                "3...7..",
                "4567654",
                "...8..3",
                "...9..2",
                ".....01",
            ),
            (5, 6),
            2,
        ),
        (
            (
                "10..9..",
                "2...8..",
                "3...7..",
                "4567654",
                "...8..3",
                "...9..2",
                ".....01",
            ),
            (1, 0),
            1,
        ),
    ),
)
def test_score_for_trailhead(given_map, given_trailhead, expected_score):
    score = day_10.trailhead_score(given_trailhead, given_map)
    assert score == expected_score


@pytest.mark.parametrize(
    "given_map, given_trailhead, expected_rating",
    (
        (
            (
                ".....0.",
                "..4321.",
                "..5..2.",
                "..6543.",
                "..7..4.",
                "..8765.",
                "..9....",
            ),
            (5, 0),
            3,
        ),
    ),
)
def test_rating_for_trailhead(given_map, given_trailhead, expected_rating):
    rating = day_10.trailhead_rating(given_trailhead, given_map)
    assert rating == expected_rating


def test_parse_input():
    parsed_input = day_10.parse_input(TEST_INPUT_1)

    assert isinstance(parsed_input, tuple)

    expected_height = 8
    assert len(parsed_input) == expected_height

    expected_width = 8
    assert all(
        isinstance(row, str) and len(row) == expected_width for row in parsed_input
    )


def test_solving_part_1_gives_expected_value():
    answer = day_10.solve_part_one(TEST_INPUT_1)
    expected_answer = 36
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_10.solve_part_two(TEST_INPUT_1)
    expected_answer = 81
    assert answer == expected_answer
