import itertools
import time
from collections import defaultdict
from pathlib import Path


def antinodes_for_antennas(antenna_positions: set, bound: complex, harmonics=False):
    antinodes = set()
    for a, b in itertools.combinations(antenna_positions, 2):
        distance = b - a
        new_antinodes = set()
        if harmonics:
            min_harmonics = 0
            max_harmonics = int(
                min(abs(bound.real // distance.real), abs(bound.imag // distance.imag))
            )
        else:
            min_harmonics = 1
            max_harmonics = 2
        for n in range(min_harmonics, max_harmonics):
            new_antinodes |= {a - distance * n, b + distance * n}

        antinodes |= new_antinodes
    return {
        a for a in antinodes if 0 <= a.real <= bound.real and 0 <= a.imag <= bound.imag
    }


def parse_input(input_path: Path):
    antennas = defaultdict(set)
    for y, row in enumerate(input_path.read_text().strip().split("\n")):
        for x, character in enumerate(row):
            if character != ".":
                antennas[character].add(complex(x, y))
    return antennas, complex(x, y)


def solve_part_one(input_path: Path):
    antennas, bound = parse_input(input_path)
    antinodes = set()
    for positions in antennas.values():
        antinodes |= antinodes_for_antennas(positions, bound)
    return len(antinodes)


def solve_part_two(input_path: Path):
    antennas, bound = parse_input(input_path)
    antinodes = set()
    for positions in antennas.values():
        antinodes |= antinodes_for_antennas(positions, bound, harmonics=True)
    return len(antinodes)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_08.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_08.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
