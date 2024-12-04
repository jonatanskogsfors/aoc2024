import itertools
from pathlib import Path

def get_x_positions(given_word_search):
    x_positions = set()
    for y, row in enumerate(given_word_search):
        for x, letter in enumerate(row):
            if letter.lower() == "x":
                x_positions.add((x, y))
    return x_positions


def mas_candidates(given_x_position):
    x, y = given_x_position
    mas_candidates = set()
    for x_delta, y_delta in itertools.product((-1, 0, +1), repeat=2):
        if x_delta == 0 and y_delta == 0:
            continue
        mas_candidates.add(frozenset(((x + x_delta * n, y + y_delta * n) for n in range(1, 4))))
    return mas_candidates

def is_mas(given_wordsearch, given_mas_candidate):
    return None

def solve_part_two(input_path: Path):
    pass


def solve_part_one(input_path: Path):
    pass


if __name__ == "__main__":
    print(solve_part_one(Path("input/input_04.txt")))
    print(solve_part_two(Path("input/input_04.txt")))


