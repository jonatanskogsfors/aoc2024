import time
from collections import defaultdict
from pathlib import Path


def blink(stones: dict):
    for stone, count in tuple(stones.items()):
        stones[stone] -= count
        if stone == 0:
            stones[1] += count
        elif len(stone_string := str(stone)) % 2 == 0:
            half = len(stone_string) // 2
            stones[int(stone_string[:half])] += count
            stones[int(stone_string[half:])] += count
        else:
            stones[stone * 2024] += count


def parse_input(input_path: Path):
    stones = tuple(map(int, input_path.read_text().strip().split()))
    return defaultdict(int, {stone: stones.count(stone) for stone in set(stones)})


def solve_part_one(input_path: Path):
    stones = parse_input(input_path)
    for _ in range(25):
        blink(stones)
    return sum(stones.values())


def solve_part_two(input_path: Path):
    stones = parse_input(input_path)
    for _ in range(75):
        blink(stones)
    return sum(stones.values())


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_11.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_11.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
