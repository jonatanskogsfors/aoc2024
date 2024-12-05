import time
from pathlib import Path


def parse_input(input_path: Path):
    rows = input_path.read_text().strip().split("\n")
    a = []
    b = []
    for row in rows:
        left, right = tuple(map(int, row.split()))
        a.append(left)
        b.append(right)
    return tuple(a), tuple(b)


def ordered_pairs(left, right):
    for a, b in zip(sorted(left), sorted(right)):
        yield a, b


def distances(left, right):
    for a, b in ordered_pairs(left, right):
        yield abs(a - b)


def similarity(number, right_list: list):
    return number * right_list.count(number)


def similarities(left, right):
    for number in left:
        yield similarity(number, right)


def solve_part_one(input_path: Path):
    left, right = parse_input(input_path)
    return sum(distances(left, right))


def solve_part_two(input_path: Path):
    left, right = parse_input(input_path)
    return sum(similarities(left, right))


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_01.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_01.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
