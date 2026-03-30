from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        for j in range(1, 10):
            for i in range(1, 10):
                s += str(self.sudoku.get((i, j), 0)) + " "
            s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        lines = s.strip().splitlines()

        for j, line in enumerate(lines, start=1):
            for i, char in enumerate(line.strip().split(), start=1):
                sudoku[i, j] = int(char)

        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}

        for atom in model:
            if atom.name == "cell" and len(atom.arguments) == 3:
                i = atom.arguments[0].number
                j = atom.arguments[1].number
                value = atom.arguments[2].number
                sudoku[i, j] = value

        return cls(sudoku)
