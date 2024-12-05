import re
import time
from pathlib import Path

MUL_PATTERN = re.compile(r"(?P<mul>mul\((\d+),(\d+)\))")
INSTRUCTIONS_PATTERN = re.compile(
    r"(?P<mul>mul\((\d+),(\d+)\))|(?P<do>do\(\))|(?P<dont>don't\(\))"
)


def multiply_match(match):
    a = match.group(2)
    b = match.group(3)
    return int(a) * int(b)


def solve_part_one(input_path: Path):
    memory = input_path.read_text()
    output = map(multiply_match, MUL_PATTERN.finditer(memory))
    return sum(output)


def solve_part_two(input_path: Path):
    memory = input_path.read_text()
    sum = 0
    do = True
    for match in INSTRUCTIONS_PATTERN.finditer(memory):
        if match.group("do"):
            do = True
        elif match.group("dont"):
            do = False
        elif match.group("mul") and do:
            sum += multiply_match(match)
    return sum


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_03.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_03.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
