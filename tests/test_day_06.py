import pytest

from aoc2024 import day_06
from aoc2024.day_06 import Direction, Guard
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_06_1.txt"


def test_guard_start_state():
    given_position = (3, 2)
    given_map = ("....", "....", "....", "....")
    given_direction = Direction.LEFT

    guard = Guard(given_position, given_direction, given_map)

    assert guard.position == given_position
    assert guard.direction == given_direction
    assert guard.lab_map == given_map
    assert guard.positions == {given_position}


def test_turn_clockwise_wraps_around():
    given_guard = Guard((0, 0), Direction.UP, ("",))
    assert given_guard.direction == Direction.UP

    given_guard.turn()
    assert given_guard.direction == Direction.RIGHT

    given_guard.turn()
    assert given_guard.direction == Direction.DOWN

    given_guard.turn()
    assert given_guard.direction == Direction.LEFT

    given_guard.turn()
    assert given_guard.direction == Direction.UP


@pytest.mark.parametrize(
    "given_position, given_direction, expected_position",
    (
        ((1, 1), Direction.UP, (1, 0)),
        ((0, 0), Direction.RIGHT, (1, 0)),
        ((1, 1), Direction.DOWN, (1, 2)),
        ((1, 1), Direction.LEFT, (0, 1)),
    ),
)
def test_next_position(given_position, given_direction, expected_position):
    given_guard = Guard(given_position, given_direction, ("",))
    next_position = given_guard.next()
    assert next_position == expected_position


@pytest.mark.parametrize(
    "given_map, given_position, expected_item",
    (
        ((".", "#"), (0, 0), "."),
        ((".", "#"), (0, 1), "#"),
        (("..#", "...", "..."), (2, 0), "#"),
        (("...", ".#.", "..."), (1, 1), "#"),
        (("...", "...", "#.."), (0, 2), "#"),
    ),
)
def test_get_position(given_map, given_position, expected_item):
    given_guard = Guard((0, 0), Direction.UP, given_map)
    item = given_guard.get_position(given_position)
    assert item == expected_item


@pytest.mark.parametrize(
    "given_map, given_position, given_direction, expected_position, expected_direction, "
    "expected_positions",
    (
        (
            ("...#",),
            (0, 0),
            Direction.RIGHT,
            (2, 0),
            Direction.DOWN,
            {(0, 0), (1, 0), (2, 0)},
        ),
    ),
)
def test_guard_move(
    given_map,
    given_position,
    given_direction,
    expected_position,
    expected_direction,
    expected_positions,
):
    given_guard = Guard(given_position, given_direction, given_map)

    given_guard.move()

    assert given_guard.position == expected_position
    assert given_guard.direction == expected_direction
    assert given_guard.positions == expected_positions


def test_parse_input():
    parsed_input = day_06.parse_input(TEST_INPUT_1)

    assert isinstance(parsed_input, Guard)
    expected_position = (4, 6)
    assert parsed_input.position == expected_position

    expected_direction = Direction.UP
    assert parsed_input.direction == expected_direction

    expected_map_width = 10
    expected_map_height = 10
    assert len(parsed_input.lab_map) == expected_map_height
    assert len(parsed_input.lab_map[0]) == expected_map_width


@pytest.mark.parametrize(
    "given_map, given_position, expected_map",
    (
        ((".",), (0, 0), ("#",)),
        (("...", "...", "..."), (1, 2), ("...", "...", ".#.")),
    ),
)
def test_add_obstacle_changes_map(given_map, given_position, expected_map):
    given_guard = Guard((0, 0), Direction.UP, given_map)

    given_guard.add_obstacle(given_position)

    assert given_guard.lab_map == expected_map


def test_loop_raises():
    given_guard = day_06.parse_input(TEST_INPUT_1)
    given_guard.add_obstacle((3, 6))
    with pytest.raises(day_06.LoopError):
        while given_guard.get_position(given_guard.next()) is not None:
            given_guard.move()


def test_solving_part_1_gives_expected_value():
    answer = day_06.solve_part_one(TEST_INPUT_1)
    expected_answer = 41
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_06.solve_part_two(TEST_INPUT_1)
    expected_answer = 6
    assert answer == expected_answer
