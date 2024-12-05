import time
from pathlib import Path


def parse_input(input_path: Path):
    pass


def solve_part_one(input_path: Path):
    pass


def solve_part_two(input_path: Path):
    pass


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_{{ '{:02}'.format(day) }}.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_{{ '{:02}'.format(day) }}.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
