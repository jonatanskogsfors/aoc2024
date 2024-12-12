import time
from pathlib import Path


def find_region(plot, garden_map):
    unvisited = {plot}
    visited = set()
    region = set()
    plant = garden_map[plot]
    while unvisited:
        candidate = unvisited.pop()
        visited.add(candidate)
        if garden_map.get(candidate) == plant:
            region.add(candidate)
            neighbors = {
                candidate + 1 + 0j,
                candidate + -1 + 0j,
                candidate + 0 + 1j,
                candidate - 0 - 1j,
            }
            unvisited |= neighbors - region - visited
    return region


def fence_price_for_region(region, bulk=False):
    area = len(region)
    left_fences = set()
    top_fences = set()
    right_fences = set()
    bottom_fences = set()
    for plot in region:
        left_fences |= {plot - 1} - region
        right_fences |= {plot + 1} - region
        top_fences |= {plot - 1j} - region
        bottom_fences |= {plot + 1j} - region
    if bulk:
        for fences in (left_fences, right_fences):
            remove = set()
            for fence in fences:
                if fence in remove:
                    continue
                for direction in (-1j, +1j):
                    neighbor = fence + direction
                    while neighbor in fences:
                        remove.add(neighbor)
                        neighbor += direction
            fences.difference_update(remove)
        for fences in (top_fences, bottom_fences):
            remove = set()
            for fence in fences:
                if fence in remove:
                    continue
                for direction in (-1, +1):
                    neighbor = fence + direction
                    while neighbor in fences:
                        remove.add(neighbor)
                        neighbor += direction
            fences.difference_update(remove)
    perimeter = (
        len(left_fences) + len(top_fences) + len(right_fences) + len(bottom_fences)
    )
    return area * perimeter


def parse_input(input_path: Path):
    return {
        complex(x, y): character
        for y, row in enumerate(input_path.read_text().strip().split("\n"))
        for x, character in enumerate(row)
    }


def solve_part_one(input_path: Path):
    garden_map = parse_input(input_path)
    categorized_plots = set()
    fence_price = 0
    for plot in garden_map:
        if plot in categorized_plots:
            continue
        region = find_region(plot, garden_map)
        categorized_plots |= region
        fence_price += fence_price_for_region(region)
    return fence_price


def solve_part_two(input_path: Path):
    garden_map = parse_input(input_path)
    categorized_plots = set()
    fence_price = 0
    for plot in garden_map:
        if plot in categorized_plots:
            continue
        region = find_region(plot, garden_map)
        categorized_plots |= region
        fence_price += fence_price_for_region(region, bulk=True)
    return fence_price


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_12.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_12.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
