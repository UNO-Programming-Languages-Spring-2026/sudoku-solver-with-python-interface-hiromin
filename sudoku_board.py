from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # Printing a str of sudoku as text in 9x9 grid format
        for j in range(1, 10):
            for i in range(1, 10):
                s += str(self.sudoku[i, j]) + " "
            s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # Create a sudoku class object from a 9x9 string representation of a sudoku puzzle
        lines = s.strip().splitlines()
        for j, line in enumerate(lines, start=1):
            for i, char in enumerate(line.strip().split(), start=1):
                sudoku[i, j] = int(char)
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # Create a sudoku class object from a clingo model
        # Look at this code. Not sure how good it is.
        for atom in model:
            if atom.name == "cell" and len(atom.arguments) == 3:
                i = atom.arguments[0].number
                j = atom.arguments[1].number
                value = atom.arguments[2].number
                sudoku[i, j] = value
        return cls(sudoku)

