import itertools
import time
from pathlib import Path

SUMMIT_HEIGHT = 9


def find_trailheads(topological_map):
    return {
        (x, y)
        for y, row in enumerate(topological_map)
        for x, char in enumerate(row)
        if char == "0"
    }


def find_paths(position, topological_map):
    x, y = position
    height = height_for_position(position, topological_map)
    return {
        (new_x, new_y)
        for dx, dy in itertools.permutations((-1, 0, 1), 2)
        if abs(dx + dy) == 1
        and height_for_position(
            ((new_x := (x + dx)), (new_y := (y + dy))), topological_map
        )
        == height + 1
    }


def height_for_position(position, topological_map):
    x, y = position
    if x < 0 or y < 0:
        return None

    try:
        value = topological_map[y][x]
        return int(value)
    except (IndexError, ValueError):
        return None


def trailhead_score(trailhead, topological_map):
    summits = set()
    unvisited = {trailhead}
    visited = set()
    while unvisited:
        position = unvisited.pop()
        visited.add(position)
        if height_for_position(position, topological_map) == SUMMIT_HEIGHT:
            summits.add(position)
        else:
            unvisited |= find_paths(position, topological_map) - visited
    return len(summits)


def trailhead_rating(trailhead, topological_map):
    summit_trails = set()
    trails = {(trailhead,)}
    while trails:
        trail = trails.pop()
        if height_for_position(trail[-1], topological_map) == SUMMIT_HEIGHT:
            summit_trails.add(trail)
        else:
            for next_position in find_paths(trail[-1], topological_map):
                trails.add((*trail, next_position))
    return len(summit_trails)


def parse_input(input_path: Path):
    return tuple(input_path.read_text().strip().split("\n"))


def solve_part_one(input_path: Path):
    topological_map = parse_input(input_path)
    return sum(
        trailhead_score(trailhead, topological_map)
        for trailhead in find_trailheads(topological_map)
    )


def solve_part_two(input_path: Path):
    topological_map = parse_input(input_path)
    return sum(
        trailhead_rating(trailhead, topological_map)
        for trailhead in find_trailheads(topological_map)
    )


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_10.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_10.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
