import pytest

from aoc2024 import day_12
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_12_1.txt"
TEST_INPUT_2 = INPUT_DIR / "test_input_12_2.txt"
TEST_INPUT_3 = INPUT_DIR / "test_input_12_3.txt"


@pytest.mark.parametrize(
    "given_map, given_position, expected_region",
    (
        ({0 + 0j: "A"}, 0 + 0j, {0, 0j}),
        (
            {0 + 0j: "A", 1 + 0j: "A", 0 + 1j: "A", 1 + 1j: "B"},
            1 + 0j,
            {0, 0j, 0, 1j, 1 + 0j},
        ),
    ),
)
def test_find_region(given_map, given_position, expected_region):
    region = day_12.find_region(given_position, given_map)
    assert region == expected_region


@pytest.mark.parametrize(
    "given_region, expected_price",
    (
        ({0 + 0j}, 1 * 4),
        ({0 + 0j, 0 + 1j, 1 + 1j, 1 + 2j}, 4 * 10),
        ({0 + 0j, 1 + 0j, 2 + 0j, 0 + 1j, 2 + 1j}, 5 * 12),
    ),
)
def test_fence_price_for_region(given_region, expected_price):
    price = day_12.fence_price_for_region(given_region)
    assert price == expected_price


@pytest.mark.parametrize(
    "given_region, expected_price",
    (
        ({0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j}, 16),
        ({0 + 0j, 1 + 0j, 0 + 1j, 1 + 1j}, 16),
        ({0 + 0j, 0 + 1j, 1 + 1j, 1 + 2j}, 32),
        ({0 + 0j}, 4),
        ({0 + 0j, 1 + 0j, 2 + 0j}, 12),
    ),
)
def test_fence_bulk_price_for_region(given_region, expected_price):
    price = day_12.fence_price_for_region(given_region, bulk=True)
    assert price == expected_price


@pytest.mark.parametrize(
    "given_input_path, expected_size",
    (
        (TEST_INPUT_1, 16),
        (TEST_INPUT_2, 25),
        (TEST_INPUT_3, 100),
    ),
)
def test_parse_input(given_input_path, expected_size):
    parsed_input = day_12.parse_input(given_input_path)
    assert isinstance(parsed_input, dict)
    assert len(parsed_input) == expected_size


@pytest.mark.parametrize(
    "given_input_path, expected_price",
    ((TEST_INPUT_1, 140), (TEST_INPUT_2, 772), (TEST_INPUT_3, 1930)),
)
def test_solving_part_1_gives_expected_value(given_input_path, expected_price):
    answer = day_12.solve_part_one(given_input_path)
    assert answer == expected_price


@pytest.mark.parametrize(
    "given_input_path, expected_price", ((TEST_INPUT_1, 80), (TEST_INPUT_3, 1206))
)
def test_solving_part_2_gives_expected_value(given_input_path, expected_price):
    answer = day_12.solve_part_two(given_input_path)
    assert answer == expected_price
