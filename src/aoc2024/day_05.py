from pathlib import Path


def parse_input(input_path: Path):
    rules_input, updates_input = input_path.read_text().strip().split("\n\n")

    rules = {tuple(map(int, rule.split("|"))) for rule in rules_input.split("\n")}

    updates = tuple(
        tuple(map(int, update.split(","))) for update in updates_input.split("\n")
    )

    return rules, updates


def is_in_order(rules: tuple[int, int], update: tuple[int]):
    for rule in rules:
        left, right = rule
        if left not in update or right not in update:
            continue
        left_index = update.index(left)
        right_index = update.index(right)

        if left_index > right_index:
            return False
    return True


def get_middle_page(given_update):
    middle_index = len(given_update) // 2
    return given_update[middle_index]


def solve_part_one(input_path: Path):
    rules, updates = parse_input(input_path)
    good_updates = [update for update in updates if is_in_order(rules, update)]
    return sum(map(get_middle_page, good_updates))


def solve_part_two(input_path: Path):
    pass


if __name__ == "__main__":
    print(solve_part_one(Path("input/input_05.txt")))
    print(solve_part_two(Path("input/input_05.txt")))
