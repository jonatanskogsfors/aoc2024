import pytest

from aoc2024 import day_20
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_20_1.txt"


@pytest.mark.parametrize(
    "given_track, given_cheat, expected_saving",
    (((1 + 1j, 1 + 2j, 2 + 2j, 3 + 2j, 3 + 1j), (2 + 1j, 3 + 1j), 2),),
)
def test_evaluate_cheat(given_track, given_cheat, expected_saving):
    saving = day_20.evaluate_cheat(given_cheat, given_track)
    assert saving == expected_saving


@pytest.mark.parametrize(
    "given_track, expected_cheats",
    (((1 + 1j, 1 + 2j, 2 + 2j, 3 + 2j, 3 + 1j), {(2 + 1j, 3 + 1j)}),),
)
def test_find_cheats(given_track, expected_cheats):
    cheats = day_20.find_cheats(given_track)
    assert cheats == expected_cheats


def test_find_all_cheats_in_test_input():
    track = day_20.parse_input(TEST_INPUT_1)
    cheats = day_20.find_cheats(track)

    expected_number_of_cheats = 44
    assert len(cheats) == expected_number_of_cheats


def test_parse_input():
    parsed_input = day_20.parse_input(TEST_INPUT_1)

    assert parsed_input
    assert isinstance(parsed_input, tuple)
    assert all(isinstance(point, complex) for point in parsed_input)


@pytest.mark.parametrize(
    "given_input, given_limit, expected_number_of_cheats",
    (
        (TEST_INPUT_1, 1, 44),
        (TEST_INPUT_1, 10, 10),
        (TEST_INPUT_1, 50, 1),
        (TEST_INPUT_1, 100, 0),
    ),
)
def test_solving_part_1_gives_expected_value(
    given_input, given_limit, expected_number_of_cheats
):
    answer = day_20.solve_part_one(given_input, limit=given_limit)
    assert answer == expected_number_of_cheats


@pytest.mark.parametrize(
    "given_input, given_limit, expected_number_of_cheats",
    ((TEST_INPUT_1, 75, 3),),
)
def test_solving_part_2_gives_expected_value(
    given_input, given_limit, expected_number_of_cheats
):
    answer = day_20.solve_part_two(given_input, limit=given_limit)
    assert answer == expected_number_of_cheats
