import time
from functools import cache
from pathlib import Path


def is_possible(design: str, stripes: tuple[str, ...]):
    for stripe in (stripe for stripe in stripes if design.startswith(stripe)):
        if stripe == design or is_possible(design[len(stripe) :], stripes):
            return True
    return False


@cache
def number_of_combinations(design: str, stripes: tuple[str, ...]):
    combinations = 0
    for stripe in (stripe for stripe in stripes if design.startswith(stripe)):
        if stripe == design:
            combinations += 1
        combinations += number_of_combinations(design[len(stripe) :], stripes)
    return combinations


def parse_input(input_path: Path):
    raw_stripes, raw_designs = input_path.read_text().strip().split("\n\n")

    stripes = tuple(stripe.strip() for stripe in raw_stripes.split(","))
    designs = tuple(raw_designs.split("\n"))

    return stripes, designs


def solve_part_one(input_path: Path):
    stripes, designs = parse_input(input_path)
    return len([design for design in designs if is_possible(design, stripes)])


def solve_part_two(input_path: Path):
    stripes, designs = parse_input(input_path)
    return sum(number_of_combinations(design, stripes) for design in designs)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_19.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_19.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
