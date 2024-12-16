import pytest

from aoc2024 import day_15
from aoc2024.day_15 import Box
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_15_1.txt"
TEST_INPUT_2 = INPUT_DIR / "test_input_15_2.txt"


def test_parse_input():
    parsed_input = day_15.parse_input(TEST_INPUT_1, scaled_up=True)

    assert len(parsed_input) == 5
    robot, boxes, walls, dimensions, moves = parsed_input

    assert isinstance(robot, complex)
    assert isinstance(boxes, dict)
    assert isinstance(walls, set)
    assert isinstance(dimensions, complex)
    assert isinstance(moves, tuple)


@pytest.mark.parametrize(
    "given_robot, given_box_positions, given_walls, given_dimensions, given_move, expected_robot, expected_box_positions",
    ((0 + 0j, {1 + 0j}, set(), 3 + 1j, day_15.RIGHT, 1 + 0j, {2 + 0j}),),
)
def test_move_thing(
    given_robot,
    given_box_positions,
    given_walls,
    given_dimensions,
    given_move,
    expected_robot,
    expected_box_positions,
):
    given_boxes = (Box(position) for position in given_box_positions)
    robot, boxes = day_15.move_thing(
        given_robot, given_move, given_boxes, given_walls, given_dimensions
    )
    assert robot == expected_robot
    assert {box.position for box in boxes} == expected_box_positions


@pytest.mark.parametrize(
    "given_input_path, expected_answer",
    (
        (TEST_INPUT_1, 2028),
        (TEST_INPUT_2, 10092),
    ),
)
def test_solving_part_1_gives_expected_value(given_input_path, expected_answer):
    answer = day_15.solve_part_one(given_input_path)
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_15.solve_part_two(TEST_INPUT_2)
    expected_answer = 9021
    assert answer == expected_answer
