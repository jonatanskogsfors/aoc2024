import re
import time
from functools import reduce
from pathlib import Path


def patrol(robot: tuple[complex, complex], given_tiles: complex, seconds: int):
    position, stride = robot
    new_x = (position.real + stride.real * seconds) % given_tiles.real
    new_y = (position.imag + stride.imag * seconds) % given_tiles.imag

    position = complex(new_x, new_y)
    return position, stride


def safety_score(robots: list[tuple[complex, complex]], tiles: complex):
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        position, _ = robot
        if position.real < tiles.real // 2 and position.imag < tiles.imag // 2:
            quadrants[0] += 1
        elif position.real > tiles.real // 2 and position.imag < tiles.imag // 2:
            quadrants[1] += 1
        elif position.real < tiles.real // 2 and position.imag > tiles.imag // 2:
            quadrants[2] += 1
        elif position.real > tiles.real // 2 and position.imag > tiles.imag // 2:
            quadrants[3] += 1
    return reduce(lambda a, b: a * b, quadrants)


def parse_input(input_path: Path):
    robot_pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    robots = []
    for match in robot_pattern.finditer(input_path.read_text()):
        robots.append(
            (
                complex(int(match.group(1)), int(match.group(2))),
                complex(int(match.group(3)), int(match.group(4))),
            )
        )
    return robots


def print_robots(robots, tiles):
    grid = []
    for n in range(int(tiles.imag)):
        grid.append([0] * int(tiles.real))
    for robot_position, _ in robots:
        grid[int(robot_position.imag)][int(robot_position.real)] += 1
    for row in grid:
        print((" ".join(map(str, row))).replace("0", "."))


def solve_part_one(input_path: Path, tiles: complex = 101 + 103j, seconds: int = 100):
    robots = parse_input(input_path)
    robots = [patrol(robot, tiles, seconds) for robot in robots]
    return safety_score(robots, tiles)


def solve_part_two(input_path: Path, tiles: complex = 101 + 103j, seconds: int = 100):
    robots = parse_input(input_path)
    robots = [patrol(robot, tiles, 6587) for robot in robots]
    print_robots(robots, tiles)
    return 6587


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_14.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_14.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
