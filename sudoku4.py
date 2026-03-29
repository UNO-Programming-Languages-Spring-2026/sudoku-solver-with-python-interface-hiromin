import sys
import clingo
from sudoku_board import Sudoku


class SudokuApp(clingo.Application):

    def __init__(self):
        self.program_name = "sudoku"

    # Load encoding and instance, then solve. 
    def main(self, ctl, files):
        ctl.load("sudoku.lp")

        for f in files:
            ctl.load(f)

        ctl.ground([("base", [])])
        ctl.solve(on_model=self.on_model)

    # Convert model to Sudoku and print formatted board.
    def on_model(self, model):
        sudoku = Sudoku.from_model(model)
        print(sudoku)


if __name__ == "__main__":
    clingo.clingo_main(SudokuApp(), sys.argv[1:])
