from enum import IntEnum


class Direction(IntEnum):
    EAST = (0,)
    SOUTH = (1,)
    WEST = (2,)
    NORTH = 3

    def turn_clockwise(self):
        return Direction((self + 1) % 4)

    def turn_counter_clockwise(self):
        return Direction((self - 1) % 4)


def manhattan(complex_distance: complex):
    return abs(complex_distance.real) + abs(complex_distance.imag)


def neighbors(position: complex):
    return {position + 1, position - 1, position + 1j, position - 1j}


def is_inside(position: complex, dimension: complex):
    return 0 <= position.real < dimension.real and 0 <= position.imag < dimension.imag
