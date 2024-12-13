import cmath
import re
import time
from pathlib import Path

A_TOKENS = 3
B_TOKENS = 1


def tokens_for_prize(
    button_a: complex, button_b: complex, prize: complex, big=False
) -> int:
    if big:
        prize += 10_000_000_000_000 + 10_000_000_000_000j

    if solution := solve_equation_system(
        (button_a.real, button_b.real, prize.real),
        (button_a.imag, button_b.imag, prize.imag),
    ):
        x, y = solution
        return x * A_TOKENS + y * B_TOKENS
    return None


def find_solution(a: complex, b: complex, c: complex) -> tuple[int, int]:
    """My initial geometric solution based on the slope of the numbers."""
    b_phase = cmath.phase(b)
    for x in range(100):
        translated_c = c - x * a
        if cmath.phase(translated_c) == b_phase:
            y = int(translated_c.real // b.real)
            return x, y
    return None


def solve_equation_system(
    equation_1: tuple[int, int, int], equation_2: tuple[int, int, int]
) -> tuple[int, int]:
    x1, y1, s1 = equation_1
    x2, y2, s2 = equation_2
    y = (s1 * x2 - s2 * x1) / (y1 * x2 - y2 * x1)
    x = (s1 - y1 * y) / x1

    if is_intish(x) and is_intish(y):
        return int(x), int(y)
    else:
        return None


def is_intish(number: float):
    very_very_little = 0.00001
    return abs(number - int(number)) < very_very_little


def parse_input(input_path: Path):
    machines = []
    number_pattern = re.compile(r"[^\d]+(\d+)[^\d]+(\d+)")
    for raw_machine in input_path.read_text().strip().split("\n\n"):
        machine = []
        for row in raw_machine.split("\n"):
            if match := number_pattern.match(row):
                machine.append(complex(int(match.group(1)), int(match.group(2))))
        machines.append(tuple(machine))

    return tuple(machines)


def solve_part_one(input_path: Path):
    machines = parse_input(input_path)
    return sum([tokens for machine in machines if (tokens := tokens_for_prize(*machine))])


def solve_part_two(input_path: Path):
    machines = parse_input(input_path)
    return sum(
        [
            tokens
            for machine in machines
            if (tokens := tokens_for_prize(*machine, big=True))
        ]
    )


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_13.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_13.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
