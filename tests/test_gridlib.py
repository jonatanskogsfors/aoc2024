import pytest

from aoc2024 import gridlib


@pytest.mark.parametrize(
    "given_complex_distance, expected_manhattan_distance",
    (
        (0 + 0j, 0),
        (1 + 0j, 1),
        (0 + 2j, 2),
        (2 + 1j, 3),
        (2 - 2j, 4),
    ),
)
def test_complex_manhattan(given_complex_distance, expected_manhattan_distance):
    manhattan_distance = gridlib.manhattan(given_complex_distance)
    assert manhattan_distance == expected_manhattan_distance


@pytest.mark.parametrize(
    "given_position, expected_neighbors", ((0 + 0j, {-1 + 0j, 1 + 0j, 0 - 1j, 0 + 1j}),)
)
def test_get_neighbors(given_position, expected_neighbors):
    neighbors = gridlib.neighbors(given_position)
    assert neighbors == expected_neighbors


@pytest.mark.parametrize(
    "given_position, given_dimension, expected_inside",
    (
        (0 + 0j, 0 + 0j, False),
        (0 + 0j, 1 + 1j, True),
        (2 + 2j, 3 + 3j, True),
        (10 + 5j, 10 + 10j, False),
        (3 - 1j, 10 + 10j, False),
        (-1 + 5j, 10 + 10j, False),
    ),
)
def test_is_inside(given_position, given_dimension, expected_inside):
    inside = gridlib.is_inside(given_position, given_dimension)
    assert inside == expected_inside
