import itertools
import time
from pathlib import Path


def dense_to_sparse_b(dense: str):
    sparse = []
    for n, (file_char, space_char) in enumerate(itertools.batched(dense + "0", 2)):
        sparse.append((n, int(file_char), int(space_char)))
    return sparse


def dense_to_sparse(dense: str):
    sparse = []
    for n, (file_char, space_char) in enumerate(itertools.batched(dense + "0", 2)):
        sparse += [f"{n}"] * int(file_char)
        sparse += ["."] * int(space_char)
    return sparse


def dense_to_intricate(dense: str):
    file_map = {}
    space_map = {}
    position = 0
    for n, (file_char, space_char) in enumerate(itertools.batched(dense + "0", 2)):
        file_length = int(file_char)
        file_map[n] = (position, file_length)
        position += file_length

        space_length = int(space_char)
        if space_length:
            space_map[position] = space_length
            position += space_length
    return file_map, space_map


def sparse_to_intricate(sparse: str):
    file_map = {}
    space_map = {}
    group_start = None
    current_char = None
    for n, char in enumerate(sparse):
        if not current_char:
            current_char = char
            group_start = n
        if char != current_char:
            if current_char == ".":
                space_map[group_start] = n - group_start
            else:
                file_map[int(current_char)] = (group_start, n - group_start)
            group_start = n
            current_char = char
    if current_char == ".":
        space_map[group_start] = n + 1 - group_start
    else:
        file_map[int(current_char)] = (group_start, n + 1 - group_start)
    return file_map, space_map


def intricate_to_sparse(file_map, space_map):
    index = 0
    sparse = []
    while index in [i for i, _ in file_map.values()] or index in space_map:
        if index in space_map:
            sparse += ["."] * space_map[index]
        else:
            for key, (start, length) in file_map.items():
                if start == index:
                    sparse += [str(key)] * length
                    break
        index = len(sparse)
    return sparse


def sparse_to_str(filesystem: list[str]):
    return "".join(filesystem)


def str_to_sparse(filesystem: str):
    return list(filesystem)


def defrag_step(filesystem, n_start=None, m_start=None):
    size = len(filesystem)
    if n_start is None:
        n_start = size
    if m_start is None:
        m_start = 0
    for n in reversed(range(n_start)):
        a_char = filesystem[n]
        if a_char == ".":
            continue
        for m in range(m_start, size):
            b_char = filesystem[m]
            if m == n:
                return filesystem, n, m
            if b_char != ".":
                continue
            filesystem[n], filesystem[m] = filesystem[m], filesystem[n]
            break
        break
    return filesystem, n, m


def find_space(file_size: int, filesystem: list[str]):
    index = sparse_to_str(filesystem).find("." * file_size)
    return index if index > -1 else None


def next_file(index, filesystem: list[str]):
    subfilesystem = filesystem[: index + 1]
    for end in reversed(range(len(subfilesystem))):
        if subfilesystem[end] == ".":
            continue
        for start in reversed(range(len(subfilesystem[: end + 1]))):
            if subfilesystem[start] != subfilesystem[end]:
                return start + 1, end + 1
            elif start == 0:
                return start, end + 1
    return None


def defrag_block(file_map, space_map):
    change = False
    for index in sorted(file_map, reverse=True):
        start, length = file_map[index]
        for space_start in sorted(space_map):
            space_length = space_map[space_start]
            if space_start > start:
                break
            if space_length >= length:
                file_map[index] = (space_start, length)
                space_map.pop(space_start)
                space_map[start] = length
                if space_length > length:
                    space_map[space_start + length] = space_length - length
                change |= True
                break
    return file_map, space_map, change


def checksum(filesystem):
    return sum(n * int(char) for n, char in enumerate(filesystem) if char != ".")


def parse_input(input_path: Path) -> str:
    return input_path.read_text().strip()


def solve_part_one(input_path: Path):
    dense_filesystem = parse_input(input_path)
    sparse_filesystem = dense_to_sparse(dense_filesystem)
    n = None
    m = None
    while True:
        sparse_filesystem, n, m = defrag_step(sparse_filesystem, n, m)
        if n == m:
            break
    return checksum(sparse_filesystem)


def solve_part_two(input_path: Path):
    dense_filesystem = parse_input(input_path)
    file_map, space_map = dense_to_intricate(dense_filesystem)
    change = True
    while change:
        file_map, space_map, change = defrag_block(file_map, space_map)
    sparse_filesystem = intricate_to_sparse(file_map, space_map)
    return checksum(sparse_filesystem)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_09.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_09.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
