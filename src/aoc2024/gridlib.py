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
