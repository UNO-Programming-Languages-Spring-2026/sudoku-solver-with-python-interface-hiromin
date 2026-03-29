import sys
import clingo
from sudoku_board import Sudoku


class Context:
    
    # Store Sudoku object for grounding.
    def __init__(self, board: Sudoku):
        self.board = board

    # Convert Sudoku board into clingo facts: initial(r,c,v)
    def initial(self):
        facts = []

        for (r, c), v in self.board.board.items():
            facts.append(
                clingo.Function(
                    "initial",
                    [clingo.Number(r), clingo.Number(c), clingo.Number(v)]
                )
            )

        return facts


class SudokuApp(clingo.Application):

    def __init__(self):
        self.program_name = "sudoku"

    # Read text input, convert to Sudoku, and solve.
    def main(self, ctl, files):
        with open(files[0]) as f:
            content = f.read()

        sudoku = Sudoku.from_str(content)
        context = Context(sudoku)

        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")

        ctl.ground([("base", [])], context=context)
        ctl.solve(on_model=self.on_model)

    # Print solved sudoku in required format.
    def on_model(self, model):
        sudoku = Sudoku.from_model(model)
        print(sudoku)


if __name__ == "__main__":
    clingo.clingo_main(SudokuApp(), sys.argv[1:])
