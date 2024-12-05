import time
from pathlib import Path


def parse_input(input_path: Path):
    rules_input, updates_input = input_path.read_text().strip().split("\n\n")

    rules = {tuple(map(int, rule.split("|"))) for rule in rules_input.split("\n")}

    updates = tuple(
        tuple(map(int, update.split(","))) for update in updates_input.split("\n")
    )

    return rules, updates


def is_in_order(rules: tuple[int, int], update: tuple[int]):
    return all(rule_holds(rule, update) for rule in rules)


def rule_holds(rule, update):
    left, right = rule
    if left not in update or right not in update:
        return True
    left_index = update.index(left)
    right_index = update.index(right)
    return left_index < right_index


def get_middle_page(given_update):
    middle_index = len(given_update) // 2
    return given_update[middle_index]


def fix_update(rules, update):
    update = list(update)
    while not is_in_order(rules, update):
        for rule in rules:
            if rule_holds(rule, update):
                continue
            left, right = rule
            left_index = update.index(left)
            right_index = update.index(right)
            update[left_index], update[right_index] = (
                update[right_index],
                update[left_index],
            )
    return tuple(update)


def solve_part_one(input_path: Path):
    rules, updates = parse_input(input_path)
    good_updates = [update for update in updates if is_in_order(rules, update)]
    return sum(map(get_middle_page, good_updates))


def solve_part_two(input_path: Path):
    rules, updates = parse_input(input_path)
    bad_updates = (update for update in updates if not is_in_order(rules, update))
    fixed_updates = (fix_update(rules, update) for update in bad_updates)
    return sum(map(get_middle_page, fixed_updates))


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_05.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_05.txt"))  # 5030 (high)
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
