import heapq
import time
from pathlib import Path

from aoc2024 import gridlib


def shortest_path(start, goal, dimension, corrupted_space):
    frontier = [(gridlib.manhattan(goal - start), 0, start)]
    best_paths = {start: ()}
    entry_count = 1
    while frontier:
        _, _, current_node = heapq.heappop(frontier)
        current_path = best_paths[current_node]
        if current_node == goal:
            return current_path
        for neighbor in gridlib.neighbors(current_node):
            if neighbor not in corrupted_space and gridlib.is_inside(neighbor, dimension):
                neighbor_path = (*current_path, neighbor)
                neighbor_score = gridlib.manhattan(goal - neighbor) + len(neighbor_path)
                if neighbor not in best_paths or len(neighbor_path) < len(
                    best_paths[neighbor]
                ):
                    best_paths[neighbor] = neighbor_path
                    heapq.heappush(frontier, (neighbor_score, entry_count, neighbor))
                    entry_count += 1
    return None


def parse_input(input_path: Path):
    return tuple(
        complex(x, y)
        for x, y in (
            map(int, row.split(",")) for row in input_path.read_text().strip().split("\n")
        )
    )


def solve_part_one(input_path: Path, dimension=71 + 71j, bytes=1024):
    corrupted_space = parse_input(input_path)
    found_path = shortest_path(
        0 + 0j, dimension - 1 - 1j, dimension, set(corrupted_space[:bytes])
    )
    return len(found_path)


def solve_part_two(input_path: Path, dimension=71 + 71j):
    corrupted_space = parse_input(input_path)
    current_path = (corrupted_space[0],)
    for n, byte in enumerate(corrupted_space):
        if byte in current_path:
            current_path = shortest_path(
                0 + 0j, dimension - 1 - 1j, dimension, set(corrupted_space[: n + 1])
            )
            if not current_path:
                return (int(byte.real), int(byte.imag))


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_18.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_18.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
