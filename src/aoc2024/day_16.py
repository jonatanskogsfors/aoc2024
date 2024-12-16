import heapq
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from aoc2024.gridlib import Direction


def get_alternatives(maze, pose):
    position, direction = pose
    alternatives = {
        (position, direction.turn_clockwise()),
        (position, direction.turn_counter_clockwise()),
    }

    match direction:
        case Direction.EAST:
            next_position = position + 1
        case Direction.SOUTH:
            next_position = position + 1j
        case Direction.WEST:
            next_position = position - 1
        case Direction.NORTH:
            next_position = position - 1j

    next_tile = maze[int(next_position.imag)][int(next_position.real)]
    if next_tile != "#":
        alternatives.add((next_position, direction))

    return alternatives


def parse_input(input_path: Path):
    position = None
    goal = None
    maze = []
    for y, row in enumerate(input_path.read_text().strip().split("\n")):
        if None in (position, goal):
            for x, tile in enumerate(row):
                if tile == "S":
                    position = complex(x, y)
                elif tile == "E":
                    goal = complex(x, y)
        maze.append(row.replace("S", "."))

    return tuple(maze), (position, Direction.EAST), goal


@dataclass(order=True)
class Node:
    pose: Any = field(compare=False)
    cost: int
    path: Any = field(compare=False)


def dijkstra(maze: tuple[str], pose: tuple[complex, Direction], goal: complex):
    visited = {}
    unvisited = []  # list[Node]

    heapq.heappush(unvisited, Node(pose, 0, {pose[0]}))

    best_score = None
    winning_paths = set()

    while unvisited:
        current_node = heapq.heappop(unvisited)
        visited[current_node.pose] = current_node
        if current_node.pose[0] == goal:
            if not best_score or current_node.cost == best_score:
                best_score = current_node.cost
                winning_paths |= current_node.path
                continue
            else:
                return best_score, winning_paths

        _, current_direction = current_node.pose
        for alternative in get_alternatives(maze, current_node.pose):
            is_unvisited = False
            for unvisited_node in unvisited:
                if unvisited_node == alternative:
                    is_unvisited = True
                    break
            if is_unvisited:
                continue

            alternative_position, alternative_direction = alternative
            step_cost = 1000 if alternative_direction != current_direction else 1
            cost = current_node.cost + step_cost
            new_node = Node(alternative, cost, current_node.path | {alternative_position})

            if visited_node := visited.get(alternative):
                if new_node.cost < visited_node.cost:
                    visited_node.cost = new_node.cost
                    visited_node.path = new_node.path
            else:
                heapq.heappush(unvisited, new_node)


def solve_part_one(input_path: Path):
    maze, pose, goal = parse_input(input_path)
    cost, _ = dijkstra(maze, pose, goal)
    return cost


def solve_part_two(input_path: Path):
    maze, pose, goal = parse_input(input_path)
    _, paths = dijkstra(maze, pose, goal)
    return len(paths)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_16.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_16.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
