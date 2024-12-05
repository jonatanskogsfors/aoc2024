import itertools
import time
from pathlib import Path


def get_positions(given_word_search, letter):
    positions = set()
    for y, row in enumerate(given_word_search):
        for x, position_letter in enumerate(row):
            if position_letter == letter:
                positions.add((x, y))
    return positions


def mas_candidates(x_position):
    x, y = x_position
    mas_candidates = set()
    for x_delta, y_delta in itertools.product((-1, 0, +1), repeat=2):
        if x_delta == 0 and y_delta == 0:
            continue
        mas_candidates.add(tuple((x + x_delta * n, y + y_delta * n) for n in range(1, 4)))
    return mas_candidates


def x_mas_candidates(a_position):
    x, y = a_position
    return {
        ((x - 1, y - 1), (x + 1, y + 1)),
        ((x - 1, y + 1), (x + 1, y - 1)),
        ((x + 1, y - 1), (x - 1, y + 1)),
        ((x + 1, y + 1), (x - 1, y - 1)),
    }


def is_mas(wordsearch, mas_candidate):
    for letter, (x, y) in zip("MAS", mas_candidate):
        if not (0 <= y < len(wordsearch) and 0 <= x < len(wordsearch[0])):
            return False
        if wordsearch[y][x] != letter:
            return False
    return True


def is_x_mas(wordsearch, x_mas_candidate):
    for letter, (x, y) in zip("MS", x_mas_candidate):
        if not (0 <= y < len(wordsearch) and 0 <= x < len(wordsearch[0])):
            return False
        if wordsearch[y][x] != letter:
            return False
    return True


def parse_input(input_path: Path):
    return tuple(input_path.read_text().strip().split("\n"))


def solve_part_one(input_path: Path):
    wordsearch = parse_input(input_path)
    x_positions = get_positions(wordsearch, "X")
    return len(
        [
            candidate
            for x in x_positions
            for candidate in mas_candidates(x)
            if is_mas(wordsearch, candidate)
        ]
    )


def solve_part_two(input_path: Path):
    wordsearch = parse_input(input_path)
    a_positions = get_positions(wordsearch, "A")
    return len(
        [
            a_position
            for a_position in a_positions
            if len(
                [
                    candidate
                    for candidate in x_mas_candidates(a_position)
                    if is_x_mas(wordsearch, candidate)
                ]
            )
            > 1
        ]
    )


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_04.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_04.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
