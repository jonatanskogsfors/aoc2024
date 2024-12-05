import time
from itertools import pairwise
from pathlib import Path


def is_safe(report, problem_dampener: bool = False):
    is_increasing = report == tuple(sorted(report))
    is_decreasing = report == tuple(sorted(report, reverse=True))

    change = [abs(b - a) for a, b in pairwise(report)]
    max_change_rate = 3
    has_gradual_change = 0 < min(change) and max(change) <= max_change_rate

    is_ok = (is_increasing or is_decreasing) and has_gradual_change

    is_ok_with_dampener = False
    if not is_ok and problem_dampener:
        for n, _ in enumerate(report):
            sub_report = report[0:n] + report[n + 1 :]
            if is_safe(sub_report):
                is_ok_with_dampener = True
                break

    return is_ok or is_ok_with_dampener


def parse_input(input_path: Path):
    reports = input_path.read_text().strip().split("\n")
    return tuple(tuple(map(int, report.split())) for report in reports)


def solve_part_one(input_path: Path):
    reports = parse_input(input_path)
    return len([report for report in reports if is_safe(report)])


def solve_part_two(input_path: Path):
    reports = parse_input(input_path)
    return len([report for report in reports if is_safe(report, problem_dampener=True)])


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_02.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_02.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
