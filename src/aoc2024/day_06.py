import time
from enum import IntEnum
from pathlib import Path


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class LoopError(Exception):
    pass


class Guard:
    def __init__(self, start_position, start_direction, lab_map):
        self._start_position = start_position
        self._start_direction = start_direction
        self._lab_map = lab_map
        self.reset()
        self.width = len(self.lab_map[0])
        self.height = len(self.lab_map)

    def reset(self):
        self._obstacle_map = None
        self.position = self._start_position
        self.direction = self._start_direction
        self.positions = {self._start_position}
        self.turn_positions = {(self.position, self.direction)}

    @property
    def lab_map(self):
        return self._obstacle_map or self._lab_map

    def patrol(self):
        while self.get_position(self.next()) is not None:
            self.move()

    def move(self):
        while (next_position := self.next()) and (
            tile := self.get_position(next_position)
        ) not in (None, "#"):
            self.position = next_position
            self.positions.add(next_position)
        if tile:
            self.turn()
            turn_position = (self.position, self.direction)
            if turn_position in self.turn_positions:
                raise LoopError()
            self.turn_positions.add(turn_position)

    def turn(self):
        self.direction = (self.direction + 1) % 4

    def next(self):
        delta_x, delta_y = ((0, -1), (1, 0), (0, 1), (-1, 0))[self.direction]
        next_x = self.position[0] + delta_x
        next_y = self.position[1] + delta_y
        return next_x, next_y

    def get_position(self, position):
        x, y = position
        if not (0 <= x < self.width and 0 <= y < self.height):
            return None
        return self.lab_map[y][x]

    def add_obstacle(self, position):
        x, y = position
        mutable_map = list(self.lab_map)
        mutable_row = list(mutable_map[y])
        mutable_row[x] = "#"
        mutable_map[y] = "".join(mutable_row)
        self._obstacle_map = tuple(mutable_map)


def parse_input(input_path: Path):
    map_with_position = input_path.read_text().strip().split("\n")
    start_position = None
    for y, row in enumerate(map_with_position):
        if "^" in row:
            start_position = row.index("^"), y
            start_direction = Direction.UP
            map_with_position[y] = row.replace("^", ".")

    lab_map = tuple(map_with_position)
    return Guard(start_position, start_direction, lab_map)


def solve_part_one(input_path: Path):
    guard = parse_input(input_path)
    guard.patrol()
    return len(guard.positions)


def solve_part_two(input_path: Path):
    guard = parse_input(input_path)
    guard.patrol()

    loop_positions = set()
    for position in tuple(guard.positions):
        guard.reset()
        guard.add_obstacle(position)
        try:
            guard.patrol()
        except LoopError:
            loop_positions.add(position)
    return len(loop_positions)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_06.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_06.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
