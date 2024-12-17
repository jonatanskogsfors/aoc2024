import time
from pathlib import Path


class Computer:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.illegal_states = set()
        self.reset()

    def reset(self):
        self.instruction_pointer = 0
        self.states = set()
        self.output = tuple()

    def run_program(self, program):
        while self.instruction_pointer < len(program) - 1:
            state = (self.a, self.b, self.c, self.instruction_pointer, tuple(self.output))
            if state in self.illegal_states:
                break
            self.states.add(state)

            opcode, operand = program[
                self.instruction_pointer : self.instruction_pointer + 2
            ]
            match opcode:
                case 0:
                    output = self.adv(operand)
                    self.instruction_pointer += 2
                case 1:
                    output = self.bxl(operand)
                    self.instruction_pointer += 2
                case 2:
                    output = self.bst(operand)
                    self.instruction_pointer += 2
                case 3:
                    output = self.jnz(operand)
                case 4:
                    output = self.bxc(operand)
                    self.instruction_pointer += 2
                case 5:
                    output = self.out(operand)
                    self.instruction_pointer += 2
                case 6:
                    output = self.bdv(operand)
                    self.instruction_pointer += 2
                case 7:
                    output = self.cdv(operand)
                    self.instruction_pointer += 2
            if output is not None:
                self.output = (*self.output, output)
                yield output

    def adv(self, operand):
        denominator = 2 ** self.combo_operand(operand)
        self.a //= denominator

    def bxl(self, operand):
        self.b ^= operand

    def bst(self, operand):
        self.b = self.combo_operand(operand) % 8

    def jnz(self, operand):
        if self.a:
            self.instruction_pointer = operand
        else:
            self.instruction_pointer += 2

    def bxc(self, operand):
        self.b ^= self.c

    def out(self, operand):
        return self.combo_operand(operand) % 8

    def bdv(self, operand):
        denominator = 2 ** self.combo_operand(operand)
        self.b = self.a // denominator

    def cdv(self, operand):
        denominator = 2 ** self.combo_operand(operand)
        self.c = self.a // denominator

    def combo_operand(self, combo_operand):
        match combo_operand:
            case literal if literal in (0, 1, 2, 3):
                value = literal
            case 4:
                value = self.a
            case 5:
                value = self.b
            case 6:
                value = self.c
        return value


def parse_input(input_path: Path):
    raw_registers, raw_program = input_path.read_text().strip().split("\n\n")

    raw_registers = raw_registers.split("\n")
    a = int(raw_registers[0].replace("Register A: ", ""))
    b = int(raw_registers[1].replace("Register B: ", ""))
    c = int(raw_registers[2].replace("Register C: ", ""))

    program = tuple(map(int, raw_program.replace("Program: ", "").split(",")))

    return a, b, c, program


def solve_part_one(input_path: Path):
    a, b, c, program = parse_input(input_path)
    computer = Computer(a, b, c)

    return ",".join(map(str, computer.run_program(program)))


def solve_part_two(input_path: Path):
    a, b, c, input_program = parse_input(input_path)
    computer = Computer(a, b, c)
    for new_a in range(0o3045130103000000, 0o3045130106000000):
        computer.reset()
        computer.a = new_a
        computer.b = b
        computer.c = c

        output_program = tuple(computer.run_program(input_program))
        if output_program == input_program:
            return new_a


def reverse_engineered(a):
    """
    24 B = A % 8
    13 B = B XOR 3
    75 C = A // 2^B
    41 B = B XOR C
    13 B = B XOR 3
    03 A = A // 2^3
    55 OUTPUT B % 8
    30 GOTO START IF A
    """
    output = []
    while a:
        b = (a % 8) ^ 3
        c = a // (2**b)
        b = b ^ c ^ 3
        a = a // 8
        output.append(b % 8)
    print(output)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_17.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1-t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_17.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3-t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3-t0:>8.3f} s")


if __name__ == "__main__":
    main()
