import itertools
import time
from pathlib import Path


def has_solution(operands, result, allowed_operators="+*"):
    for operators in itertools.product(allowed_operators, repeat=len(operands) - 1):
        cumulative_sum, *other_operands = operands
        for operator, operand in zip(operators, other_operands):
            match operator:
                case "+":
                    cumulative_sum += operand
                case "*":
                    cumulative_sum *= operand
                case "|":
                    cumulative_sum = int(f"{cumulative_sum}{operand}")
        if cumulative_sum == result:
            return True
    return False


def parse_input(input_path: Path):
    raw_rows = input_path.read_text().strip().split("\n")
    rows = []
    for row in raw_rows:
        result, operands = row.split(":")
        rows.append((int(result), tuple(map(int, operands.strip().split()))))
    return tuple(rows)


def solve_part_one(input_path: Path):
    equations = parse_input(input_path)
    return sum(result for result, operands in equations if has_solution(operands, result))


def solve_part_two(input_path: Path):
    equations = parse_input(input_path)
    return sum(
        result
        for result, operands in equations
        if has_solution(operands, result, allowed_operators="+*|")
    )


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_07.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_07.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
