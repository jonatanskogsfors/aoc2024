import time
from pathlib import Path

from aoc2024 import gridlib


def find_cheats(track, limit=2):
    cheats = set()
    track_points = set(track)
    for n, point in enumerate(track):
        for neighbor in gridlib.neighbors(point) - track_points:
            cheats |= recursive_cheat_finder(
                track[: n + 2], track[n + 2 :], (neighbor,), neighbor, limit
            )
    return {(cheat[0], cheat[-1]) for cheat in cheats}


def find_cheats_old(track):
    cheats = set()
    track_points = set(track)
    for n, point in enumerate(track):
        for neighbor in gridlib.neighbors(point) - track_points:
            for neighbors_neighbor in gridlib.neighbors(neighbor):
                if neighbors_neighbor in track[n + 3 :]:
                    cheats.add((neighbor, neighbors_neighbor))
    return cheats


def recursive_cheat_finder(track_behind, track_in_front, cheat, position, step):
    cheats = set()
    if step == 0:
        return cheats
    if position in track_in_front:
        cheats.add(cheat)
        return cheats
    for neighbor in gridlib.neighbors(position):
        extended_cheat = (*cheat, neighbor)
        if neighbor in track_behind:
            continue
        cheats |= recursive_cheat_finder(
            track_behind + track_in_front[:1],
            track_in_front[1:],
            extended_cheat,
            neighbor,
            step - 1,
        )
    return cheats


def evaluate_cheat(cheat: tuple[complex, complex], track: tuple):
    cheat_start, cheat_end = cheat
    for n, point in enumerate(track):
        if cheat_start in gridlib.neighbors(point):
            end_n = track.index(cheat_end)
            return end_n - (n + 2)


def parse_input(input_path: Path):
    raw_track = tuple(input_path.read_text().strip().split("\n"))
    start = None
    end = None
    for y, row in enumerate(raw_track):
        for x, char in enumerate(row):
            if char == "S":
                start = complex(x, y)
            elif char == "E":
                end = complex(x, y)
            if start and end:
                break
    track = [start]
    current = start
    while current != end:
        for neighbor in gridlib.neighbors(current):
            if (
                neighbor not in track
                and raw_track[int(neighbor.imag)][int(neighbor.real)] in ".E"
            ):
                track.append(neighbor)
                current = neighbor
    return tuple(track)


def solve_part_one(input_path: Path, limit=100):
    track = parse_input(input_path)
    cheats = find_cheats(track)
    return len([cheat for cheat in cheats if evaluate_cheat(cheat, track) >= limit])


def solve_part_two(input_path: Path, limit=100):
    track = parse_input(input_path)
    cheats = find_cheats(track, 20)
    return len([cheat for cheat in cheats if evaluate_cheat(cheat, track) >= limit])


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_20.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_20.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
