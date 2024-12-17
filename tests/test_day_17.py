import pytest

from aoc2024 import day_17
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_17_1.txt"
TEST_INPUT_2 = INPUT_DIR / "test_input_17_2.txt"


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_value",
    (
        ((7, 7, 7), 0, 0),
        ((7, 7, 7), 1, 1),
        ((7, 7, 7), 2, 2),
        ((7, 7, 7), 3, 3),
        ((7, 0, 0), 4, 7),
        ((0, 6, 0), 5, 6),
        ((0, 0, 5), 6, 5),
    ),
)
def test_combo_operator(given_registers, given_operand, expected_value):
    given_computer = day_17.Computer(*given_registers)
    combo_value = given_computer.combo_operand(given_operand)
    assert combo_value == expected_value


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_registers",
    (
        ((5, 0, 0), 0, (5, 0, 0)),
        ((7, 0, 0), 1, (3, 0, 0)),
        ((7, 0, 0), 2, (1, 0, 0)),
        ((2, 0, 0), 3, (0, 0, 0)),
        ((3, 0, 0), 4, (0, 0, 0)),
        ((7, 1, 0), 5, (3, 1, 0)),
        ((5, 0, 1), 6, (2, 0, 1)),
    ),
)
def test_test_adv_instruction(given_registers, given_operand, expected_registers):
    given_computer = day_17.Computer(*given_registers)
    given_computer.adv(given_operand)
    expected_register_a, expected_register_b, expected_register_c = expected_registers
    assert given_computer.a == expected_register_a
    assert given_computer.b == expected_register_b
    assert given_computer.c == expected_register_c


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_registers",
    (
        ((0, 1, 0), 0, (0, 1, 0)),
        ((0, 2, 0), 1, (0, 3, 0)),
        ((0, 3, 0), 2, (0, 1, 0)),
        ((0, 4, 0), 3, (0, 7, 0)),
        ((0, 5, 0), 4, (0, 1, 0)),
        ((0, 6, 0), 5, (0, 3, 0)),
        ((0, 7, 0), 6, (0, 1, 0)),
        ((0, 0, 0), 7, (0, 7, 0)),
    ),
)
def test_bxl_operator(given_registers, given_operand, expected_registers):
    given_computer = day_17.Computer(*given_registers)
    given_computer.bxl(given_operand)
    expected_register_a, expected_register_b, expected_register_c = expected_registers
    assert given_computer.a == expected_register_a
    assert given_computer.b == expected_register_b
    assert given_computer.c == expected_register_c


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_registers",
    (
        ((0, 0, 0), 0, (0, 0, 0)),
        ((0, 0, 0), 1, (0, 1, 0)),
        ((0, 0, 0), 2, (0, 2, 0)),
        ((0, 0, 0), 3, (0, 3, 0)),
        ((7, 0, 0), 4, (7, 7, 0)),
        ((0, 6, 0), 5, (0, 6, 0)),
        ((0, 0, 5), 6, (0, 5, 5)),
    ),
)
def test_bst_operator(given_registers, given_operand, expected_registers):
    given_computer = day_17.Computer(*given_registers)
    given_computer.bst(given_operand)
    expected_register_a, expected_register_b, expected_register_c = expected_registers
    assert given_computer.a == expected_register_a
    assert given_computer.b == expected_register_b
    assert given_computer.c == expected_register_c


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_registers, expected_instruction_pointer",
    (
        ((0, 0, 0), 0, (0, 0, 0), 2),
        ((7, 0, 0), 1, (7, 0, 0), 1),
        ((6, 0, 0), 2, (6, 0, 0), 2),
        ((5, 0, 0), 3, (5, 0, 0), 3),
        ((4, 0, 0), 4, (4, 0, 0), 4),
        ((3, 0, 0), 5, (3, 0, 0), 5),
        ((2, 0, 0), 6, (2, 0, 0), 6),
        ((1, 0, 0), 7, (1, 0, 0), 7),
    ),
)
def test_jnz_operator(
    given_registers, given_operand, expected_registers, expected_instruction_pointer
):
    given_computer = day_17.Computer(*given_registers)
    given_computer.jnz(given_operand)
    expected_register_a, expected_register_b, expected_register_c = expected_registers

    assert given_computer.instruction_pointer == expected_instruction_pointer

    assert given_computer.a == expected_register_a
    assert given_computer.b == expected_register_b
    assert given_computer.c == expected_register_c


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_registers",
    (
        ((0, 7, 3), 0, (0, 4, 3)),
        ((0, 6, 4), 1, (0, 2, 4)),
        ((0, 5, 5), 2, (0, 0, 5)),
        ((0, 4, 6), 3, (0, 2, 6)),
        ((0, 3, 7), 4, (0, 4, 7)),
        ((0, 2, 0), 5, (0, 2, 0)),
        ((0, 1, 1), 6, (0, 0, 1)),
        ((0, 0, 2), 7, (0, 2, 2)),
    ),
)
def test_bxc_operator(given_registers, given_operand, expected_registers):
    given_computer = day_17.Computer(*given_registers)
    given_computer.bxc(given_operand)
    expected_register_a, expected_register_b, expected_register_c = expected_registers
    assert given_computer.a == expected_register_a
    assert given_computer.b == expected_register_b
    assert given_computer.c == expected_register_c


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_registers, expected_output",
    (
        ((0, 0, 0), 0, (0, 0, 0), 0),
        ((0, 0, 0), 1, (0, 0, 0), 1),
        ((0, 0, 0), 2, (0, 0, 0), 2),
        ((0, 0, 0), 3, (0, 0, 0), 3),
        ((7, 0, 0), 4, (7, 0, 0), 7),
        ((0, 5, 0), 5, (0, 5, 0), 5),
        ((0, 0, 4), 6, (0, 0, 4), 4),
    ),
)
def test_out_operator(
    given_registers, given_operand, expected_registers, expected_output
):
    given_computer = day_17.Computer(*given_registers)
    output = given_computer.out(given_operand)

    assert output == expected_output

    expected_register_a, expected_register_b, expected_register_c = expected_registers
    assert given_computer.a == expected_register_a
    assert given_computer.b == expected_register_b
    assert given_computer.c == expected_register_c


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_registers",
    (
        ((5, 0, 0), 0, (5, 5, 0)),
        ((7, 0, 0), 1, (7, 3, 0)),
        ((7, 0, 0), 2, (7, 1, 0)),
        ((2, 0, 0), 3, (2, 0, 0)),
        ((3, 0, 0), 4, (3, 0, 0)),
        ((7, 1, 0), 5, (7, 3, 0)),
        ((5, 0, 1), 6, (5, 2, 1)),
    ),
)
def test_test_bdv_instruction(given_registers, given_operand, expected_registers):
    given_computer = day_17.Computer(*given_registers)

    given_computer.bdv(given_operand)

    expected_register_a, expected_register_b, expected_register_c = expected_registers
    assert given_computer.a == expected_register_a
    assert given_computer.b == expected_register_b
    assert given_computer.c == expected_register_c


@pytest.mark.parametrize(
    "given_registers, given_operand, expected_registers",
    (
        ((5, 0, 0), 0, (5, 0, 5)),
        ((7, 0, 0), 1, (7, 0, 3)),
        ((7, 0, 0), 2, (7, 0, 1)),
        ((2, 0, 0), 3, (2, 0, 0)),
        ((3, 0, 0), 4, (3, 0, 0)),
        ((7, 1, 0), 5, (7, 1, 3)),
        ((5, 0, 1), 6, (5, 0, 2)),
    ),
)
def test_test_cdv_instruction(given_registers, given_operand, expected_registers):
    given_computer = day_17.Computer(*given_registers)

    given_computer.cdv(given_operand)

    expected_register_a, expected_register_b, expected_register_c = expected_registers
    assert given_computer.a == expected_register_a
    assert given_computer.b == expected_register_b
    assert given_computer.c == expected_register_c


def test_parse_input():
    parsed_input = day_17.parse_input(TEST_INPUT_1)

    expected_input_length = 4
    assert len(parsed_input) == expected_input_length
    a, b, c, program = parsed_input

    expected_a = 729
    assert a == expected_a

    expected_b = 0
    assert b == expected_b

    expected_c = 0
    assert c == expected_c

    expected_program = (0, 1, 5, 4, 3, 0)
    assert program == expected_program


def test_solving_part_1_gives_expected_value():
    answer = day_17.solve_part_one(TEST_INPUT_1)
    expected_answer = "4,6,3,5,6,3,5,2,1,0"
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_17.solve_part_two(TEST_INPUT_2)
    expected_answer = 117440
    assert answer == expected_answer
