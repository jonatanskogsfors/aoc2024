import re
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


if __name__ == "__main__":
    print(solve_part_one(Path("input/input_03.txt")))
    print(solve_part_two(Path("input/input_03.txt")))
