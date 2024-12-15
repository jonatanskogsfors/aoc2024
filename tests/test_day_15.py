from pathlib import Path

import pytest

from aoc2024 import day_15
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_15_1.txt"
TEST_INPUT_2 = INPUT_DIR / "test_input_15_2.txt"

@pytest.mark.parametrize(
    "given_robot, given_direction, given_dimensions, expected_robot",
    (
        (0+0j, day_15.RIGHT, 2+1j, 1+0j),  # Right ok
        (0+0j, day_15.RIGHT, 1+1j, 0+0j),  # Right not ok
        (1+0j, day_15.LEFT, 2+1j, 0+0j),  # Left ok
        (0+0j, day_15.LEFT, 1+1j, 0+0j), # Left not ok
        (0+1j, day_15.UP, 1+2j, 0+0j),  # Up ok
        (0+0j, day_15.UP, 1+1j, 0+0j),  # Up not ok
        (0+0j, day_15.DOWN, 1+2j, 0+1j),  # Down ok
        (0+0j, day_15.DOWN, 1+1j, 0+0j),  # Down not ok
    ),
)
def test_move_thing_without_walls_or_boxes(given_robot, given_direction, given_dimensions, expected_robot):
    given_boxes = set()
    given_walls = set()
    robot, boxes = day_15.move_thing(given_robot, given_direction, given_boxes, given_walls, given_dimensions)
    assert robot == expected_robot
    assert boxes == given_boxes

@pytest.mark.parametrize(
    "given_robot, given_direction, given_walls, given_dimensions, expected_robot",
    (
        (0+0j, day_15.RIGHT, {1+0j}, 5+1j, 0+0j), # Right not ok
    ),
)
def test_move_thing_with_walls(given_robot, given_direction, given_walls, given_dimensions, expected_robot):
    given_boxes = set()
    robot, boxes = day_15.move_thing(given_robot, given_direction, given_boxes, given_walls, given_dimensions)
    assert robot == expected_robot
    assert boxes == given_boxes

@pytest.mark.parametrize(
    "given_robot, given_direction, given_boxes, given_dimensions, expected_robot, expected_boxes",
    (
        (0+0j, day_15.RIGHT, {1+0j}, 3+1j, 1+0j, {2+0j}),  # Right ok
        (0+0j, day_15.DOWN, {0+1j, 0+2j}, 1+4j, 0+1j, {0+2j, 0+3j}),  # Down ok
        (1+0j, day_15.LEFT, {0+0j}, 2+1j, 1+0j, {0+0j}),  # Left not ok
    ),
)
def test_move_things_with_boxes(given_robot, given_direction, given_boxes, given_dimensions, expected_robot, expected_boxes):
    given_walls = set()
    robot, boxes = day_15.move_thing(given_robot, given_direction, given_boxes, given_walls, given_dimensions)
    assert robot == expected_robot
    assert boxes == expected_boxes

@pytest.mark.parametrize(
    "given_robot, given_direction, given_boxes, given_dimensions, expected_robot, expected_boxes",
    (
        (0+0j, day_15.RIGHT, {1+0j}, 3+1j, 1+0j, {2+0j}),  # Right ok
        (0+0j, day_15.DOWN, {0+1j, 0+2j}, 1+4j, 0+1j, {0+2j, 0+3j}),  # Down ok
        (3+0j, day_15.LEFT, {1+0j}, 4+1j, 2+0j, {0+0j}), # Left ok
        (0+3j, day_15.UP, {0+1j}, 1+4j, 0+2j, {0+0j}), # Up ok
    ),
)
def test_move_scaled_up_things_with_boxes(given_robot, given_direction, given_boxes, given_dimensions, expected_robot, expected_boxes):
    given_walls = set()
    robot, boxes = day_15.move_thing(given_robot, given_direction, given_boxes, given_walls, given_dimensions, scaled_up=True)
    assert robot == expected_robot
    assert boxes == expected_boxes

def test_parse_input():
    parsed_input = day_15.parse_input(TEST_INPUT_1)
    expected_robot = 2+2j
    expected_boxes = {3+1j, 5+1j, 4+2j, 4+3j, 4+4j, 4+5j}

    expected_walls = {1+2j,2+4j}
    expected_walls |= {complex(x, y) for y in (0, 7) for x in range(8)}
    expected_walls |= {complex(x, y) for y in range(8) for x in (0, 7)}

    expected_dimensions = 8+8j
    expected_moves = (
        day_15.LEFT,
        day_15.UP,
        day_15.UP,
        day_15.RIGHT,
        day_15.RIGHT,
        day_15.RIGHT,
        day_15.DOWN,
        day_15.DOWN,
        day_15.LEFT,
        day_15.DOWN,
        day_15.RIGHT,
        day_15.RIGHT,
        day_15.DOWN,
        day_15.LEFT,
        day_15.LEFT
    )


    assert len(parsed_input) == 5
    robot, boxes, walls, dimensions, moves = parsed_input

    assert robot == expected_robot
    assert boxes == expected_boxes
    assert walls == expected_walls
    assert dimensions == expected_dimensions
    assert moves == expected_moves

def test_parse_scaled_up_input():
    parsed_input = day_15.parse_input(TEST_INPUT_1, scaled_up=True)
    expected_robot = 4+2j
    expected_boxes = {(6+1j, 7+1j), (10+1j, 11+1j), (8+2j, 9+2j), (8+3j, 9+3j), (8+4j, 9+4j), (8+5j, 9+5j)}

    expected_walls = {2+2j, 3+2j, 4+4j, 5+4j}
    expected_walls |= {complex(x, y) for y in (0, 7) for x in range(16)}
    expected_walls |= {complex(x, y) for y in range(8) for x in (0, 1, 14, 15)}
    expected_dimensions = 16+8j
    expected_moves = (
        day_15.LEFT,
        day_15.UP,
        day_15.UP,
        day_15.RIGHT,
        day_15.RIGHT,
        day_15.RIGHT,
        day_15.DOWN,
        day_15.DOWN,
        day_15.LEFT,
        day_15.DOWN,
        day_15.RIGHT,
        day_15.RIGHT,
        day_15.DOWN,
        day_15.LEFT,
        day_15.LEFT
    )


    assert len(parsed_input) == 5
    robot, boxes, walls, dimensions, moves = parsed_input

    assert robot == expected_robot
    assert boxes == expected_boxes
    assert walls == expected_walls
    assert dimensions == expected_dimensions
    assert moves == expected_moves


@pytest.mark.parametrize(
    "given_input_path, expected_answer",
    (
            (TEST_INPUT_1, 2028),
            (TEST_INPUT_2, 10092),
    )
)
def test_solving_part_1_gives_expected_value(given_input_path, expected_answer):
    answer = day_15.solve_part_one(given_input_path)
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_15.solve_part_two(TEST_INPUT_2)
    expected_answer = 9021
    assert answer == expected_answer