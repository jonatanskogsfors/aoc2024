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


if __name__ == "__main__":
    print(solve_part_one(Path("input/input_01.txt")))
    print(solve_part_two(Path("input/input_01.txt")))
