import pytest

from aoc2024 import day_14
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_14_1.txt"


@pytest.mark.parametrize(
    "given_robot, given_tiles, given_seconds, expected_position",
    (
        ((0 + 0j, 1 + 1j), 11 + 7j, 1, 1 + 1j),
        ((2 + 4j, 2 - 3j), 11 + 7j, 1, 4 + 1j),
        ((2 + 4j, 2 - 3j), 11 + 7j, 2, 6 + 5j),
        ((2 + 4j, 2 - 3j), 11 + 7j, 3, 8 + 2j),
        ((2 + 4j, 2 - 3j), 11 + 7j, 4, 10 + 6j),
        ((2 + 4j, 2 - 3j), 11 + 7j, 5, 1 + 3j),
    ),
)
def test_robot_movement(given_robot, given_tiles, given_seconds, expected_position):
    robot = day_14.patrol(given_robot, given_tiles, given_seconds)
    assert robot[0] == expected_position


@pytest.mark.parametrize(
    "given_robots, given_tiles, expected_safety_score",
    (
        (
            ((0 + 0j, 0 + 0j), (2 + 0j, 0 + 0j), (0 + 2j, 0 + 0j), (2 + 2j, 0 + 0j)),
            3 + 3j,
            1,
        ),
        (((0 + 0j, 0 + 0j), (2 + 0j, 0 + 0j), (0 + 2j, 0 + 0j)), 3 + 3j, 0),
        (
            (
                (0 + 0j, 0 + 0j),
                (2 + 0j, 0 + 0j),
                (2 + 0j, 0 + 0j),
                (0 + 2j, 0 + 0j),
                (2 + 2j, 0 + 0j),
            ),
            3 + 3j,
            2,
        ),
        (
            (
                (0 + 0j, 0 + 0j),
                (2 + 0j, 0 + 0j),
                (1 + 1j, 1 + 1j),
                (0 + 2j, 0 + 0j),
                (2 + 2j, 0 + 0j),
            ),
            3 + 3j,
            1,
        ),
    ),
)
def test_safety_factor(given_robots, given_tiles, expected_safety_score):
    safety_score = day_14.safety_score(given_robots, given_tiles)
    assert safety_score == expected_safety_score


def test_parse_input():
    parsed_input = day_14.parse_input(TEST_INPUT_1)
    expected_number_of_robots = 12
    assert len(parsed_input) == expected_number_of_robots
    assert isinstance(parsed_input, list)
    assert all(isinstance(robot, tuple) for robot in parsed_input)
    assert all(
        isinstance(component, complex) for robot in parsed_input for component in robot
    )


def test_solving_part_1_gives_expected_value():
    given_tiles = 11 + 7j
    answer = day_14.solve_part_one(TEST_INPUT_1, tiles=given_tiles)
    expected_answer = 12
    assert answer == expected_answer
