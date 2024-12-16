import pytest

from aoc2024 import day_16
from aoc2024.gridlib import Direction
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_16_1.txt"
TEST_INPUT_2 = INPUT_DIR / "test_input_16_2.txt"


@pytest.mark.parametrize(
    "given_maze, given_position, expected_alternatives",
    (
        (
            ("#####", "#...#", "#.#.#", "#####"),
            (1 + 1j, Direction.EAST),
            {
                (1 + 1j, Direction.NORTH),
                (1 + 1j, Direction.SOUTH),
                ((2 + 1j, Direction.EAST)),
            },
        ),
    ),
)
def test_find_neighbors(given_maze, given_position, expected_alternatives):
    alternatives = day_16.get_alternatives(given_maze, given_position)
    assert alternatives == expected_alternatives


def test_parse_input():
    parsed_input = day_16.parse_input(TEST_INPUT_1)
    expected_parts = 3
    assert len(parsed_input) == expected_parts
    maze, pose, goal = parsed_input

    assert maze
    assert isinstance(maze, tuple)
    assert all(isinstance(row, str) for row in maze)

    assert isinstance(pose, tuple)
    position, direction = pose
    assert isinstance(position, complex)
    assert isinstance(direction, Direction)

    assert isinstance(goal, complex)


@pytest.mark.parametrize(
    "given_input_path, expected_answer",
    (
        (TEST_INPUT_1, 7036),
        (TEST_INPUT_2, 11048),
    ),
)
def test_solving_part_1_gives_expected_value(given_input_path, expected_answer):
    answer = day_16.solve_part_one(given_input_path)
    assert answer == expected_answer


@pytest.mark.parametrize(
    "given_input_path, expected_answer",
    (
        (TEST_INPUT_1, 45),
        (TEST_INPUT_2, 64),
    ),
)
def test_solving_part_2_gives_expected_value(given_input_path, expected_answer):
    answer = day_16.solve_part_two(given_input_path)
    assert answer == expected_answer
