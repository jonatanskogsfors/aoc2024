from pathlib import Path

__all__ = [module.stem for module in Path(__file__).parent.glob("day_*.py")]

ROOT_DIR = Path(__file__).parent
TEST_DIR = Path(__file__).parent.parent.parent / "tests"

from aoc2024 import *
