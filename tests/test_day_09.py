import pytest

from aoc2024 import day_09
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_09_1.txt"


@pytest.mark.parametrize("given_dense, expected_sparse", (("12345", "0..111....22222"),))
def test_dense_to_sparse(given_dense, expected_sparse):
    sparse = day_09.dense_to_sparse(given_dense)
    sparse = day_09.sparse_to_str(sparse)
    assert sparse == expected_sparse


@pytest.mark.parametrize(
    "given_dense, expected_file_map, expected_space_list",
    (("12345", {0: (0, 1), 1: (3, 3), 2: (10, 5)}, {1: 2, 6: 4}),),
)
def test_dense_to_intricate(given_dense, expected_file_map, expected_space_list):
    file_map, space_list = day_09.dense_to_intricate(given_dense)
    assert file_map == expected_file_map
    assert space_list == expected_space_list


@pytest.mark.parametrize(
    "given_sparse, expected_file_map, expected_space_map",
    (("0..111....22222", {0: (0, 1), 1: (3, 3), 2: (10, 5)}, {1: 2, 6: 4}),),
)
def test_sparse_to_intricate(given_sparse, expected_file_map, expected_space_map):
    file_map, space_map = day_09.sparse_to_intricate(given_sparse)
    assert file_map == expected_file_map
    assert space_map == expected_space_map


@pytest.mark.parametrize(
    "given_file_map, given_space_map, expected_sparse",
    (({0: (0, 1), 1: (3, 3), 2: (10, 5)}, {1: 2, 6: 4}, "0..111....22222"),),
)
def test_intricate_to_sparse(given_file_map, given_space_map, expected_sparse):
    sparse = day_09.intricate_to_sparse(given_file_map, given_space_map)
    assert day_09.sparse_to_str(sparse) == expected_sparse


@pytest.mark.parametrize(
    "given_filesystem, expected_filesystem",
    (("0..111....22222", "02.111....2222."), ("022111222......", "022111222......")),
)
def test_defrag_step(given_filesystem, expected_filesystem):
    given_filesystem = day_09.str_to_sparse(given_filesystem)
    defragged_filesystem, _, _ = day_09.defrag_step(given_filesystem)
    defragged_filesystem = day_09.sparse_to_str(defragged_filesystem)
    assert defragged_filesystem == expected_filesystem


@pytest.mark.parametrize(
    "given_filesize, given_filesystem, expected_position",
    (
        (1, ".", 0),
        (1, "0.", 1),
        (2, ".0..", 2),
        (3, ".0..1111.", None),
    ),
)
def test_find_space(given_filesize, given_filesystem, expected_position):
    given_filesystem = day_09.str_to_sparse(given_filesystem)
    position = day_09.find_space(given_filesize, given_filesystem)
    assert position == expected_position


@pytest.mark.parametrize(
    "given_index, given_filesystem, expected_positions",
    (
        (0, "0", (0, 1)),
        (1, "0.", (0, 1)),
        (1, "01", (1, 2)),
        (5, "00.111222", (3, 6)),
        (0, ".", None),
        (2, "...000", None),
    ),
)
def test_next_file(given_index, given_filesystem, expected_positions):
    given_filesystem = day_09.str_to_sparse(given_filesystem)
    positions = day_09.next_file(given_index, given_filesystem)
    assert positions == expected_positions


@pytest.mark.parametrize(
    "given_filesystem, expected_filesystem",
    (
        (
            "00...111...2...333.44.5555.6666.777.888899",
            "00992111777.44.333....5555.6666.....8888..",
        ),
    ),
)
def test_defrag_block(given_filesystem, expected_filesystem):
    file_map, space_map = day_09.sparse_to_intricate(given_filesystem)

    file_map, space_map, _ = day_09.defrag_block(file_map, space_map)

    sparse = day_09.intricate_to_sparse(file_map, space_map)
    sparse = day_09.sparse_to_str(sparse)
    assert sparse == expected_filesystem


@pytest.mark.parametrize(
    "given_filesystem, expected_checksum",
    (("0099811188827773336446555566..............", 1928),),
)
def test_checksum(given_filesystem, expected_checksum):
    given_filesystem = list(given_filesystem)
    checksum = day_09.checksum(given_filesystem)
    assert checksum == expected_checksum


def test_parse_input():
    parsed_input = day_09.parse_input(TEST_INPUT_1)
    assert isinstance(parsed_input, str)
    assert all(char.isdigit() for char in parsed_input)


def test_solving_part_1_gives_expected_value():
    answer = day_09.solve_part_one(TEST_INPUT_1)
    expected_answer = 1928
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_09.solve_part_two(TEST_INPUT_1)
    expected_answer = 2858
    assert answer == expected_answer
