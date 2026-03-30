from typing import Tuple
import clingo


class Sudoku:
    # Initializes Sudoku from a dictionary of (col, row) -> value
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    # Converts Sudoku object into a readable 9x9 string
    def __str__(self) -> str:
        result = []

        # Loop through rows (1 to 9)
        for j in range(1, 10):
            row = []

            # Loop through columns (1 to 9)
            for i in range(1, 10):
                # Use 0 if cell is missing (avoids KeyError)
                row.append(str(self.sudoku.get((i, j), 0)))

            result.append(" ".join(row))

        return "\n".join(result)

    # Builds Sudoku from a 9x9 whitespace-separated string
    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}

        lines = s.strip().splitlines()

        # Convert each line into row values
        for j, line in enumerate(lines, start=1):
            values = line.strip().split()

            for i, val in enumerate(values, start=1):
                sudoku[(i, j)] = int(val)

        return cls(sudoku)

    # Builds Sudoku from a Clingo model
    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}

        # Extract only atoms marked as "shown"
        for atom in model.symbols(shown=True):

            # Expect predicate: cell(i, j, value)
            if atom.name == "cell" and len(atom.arguments) == 3:
                i = atom.arguments[0].number
                j = atom.arguments[1].number
                value = atom.arguments[2].number

                sudoku[(i, j)] = value

        return cls(sudoku)
