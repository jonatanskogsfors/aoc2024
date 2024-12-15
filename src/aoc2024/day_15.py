import os
import time
from pathlib import Path

RIGHT = 1+0j
DOWN = 0+1j
LEFT = -1+0j
UP = 0-1j

DIRECTION = {
    "^": UP,
    ">": RIGHT,
    "v": DOWN,
    "<": LEFT
}

def move_thing(thing: complex, direction: complex, boxes: set, walls: set, dimensions: complex, scaled_up=False):
    new_thing = thing + direction
    inside_bounds = (
            0 <= new_thing.real < dimensions.real
            and 0 <= new_thing.imag < dimensions.imag
    )


    blocked_by_walls = new_thing in walls

    blocked_by_things = False

    box_check = new_thing

    if box_check in boxes:
        boxes.discard(box_check)
        new_box, boxes = move_thing(box_check, direction, boxes, walls, dimensions)
        boxes.add(new_box)
        if new_box == box_check:
            blocked_by_things = True

    if not inside_bounds or blocked_by_walls or blocked_by_things:
        new_thing = thing
    return new_thing, boxes


def parse_input(input_path: Path, scaled_up=False):
    raw_map, raw_moves = input_path.read_text().strip().split("\n\n")
    robot = None
    boxes = set()
    walls = set()

    x_scaler = 1 + scaled_up

    for y, row in enumerate(raw_map.split("\n")):
        for x, char in enumerate(row):
            match char:
                case "@":
                    robot = complex(x * x_scaler, y)
                case "O":
                    if scaled_up:
                        boxes.add((complex(x * x_scaler, y), complex((x * x_scaler) + 1, y)))
                    else:
                        boxes.add(complex(x * x_scaler, y))
                case "#":
                    walls.add(complex(x * x_scaler, y))
                    if scaled_up:
                        walls.add(complex((x * x_scaler) + 1, y))

    dimensions = complex((x+1) * x_scaler, y+1)

    moves = tuple(DIRECTION[move] for move in raw_moves.replace("\n", ""))
    return robot, boxes, walls, dimensions, moves


def solve_part_one(input_path: Path):
    robot, boxes, walls, dimensions, moves = parse_input(input_path)
    for move in moves:
        robot, boxes = move_thing(robot, move, boxes, walls, dimensions)
    return sum(int(box.imag * 100 + box.real) for box in boxes)

def solve_part_two(input_path: Path):
    robot, boxes, walls, dimensions, moves = parse_input(input_path, scaled_up=True)
    for move in moves:
        robot, boxes = move_thing(robot, move, boxes, walls, dimensions, scaled_up=True)
    return sum(int(box.imag * 100 + box.real) for box in boxes)

def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_15.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_15.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
