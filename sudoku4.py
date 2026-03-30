import sys
import clingo
from sudoku_board import Sudoku

class SudokuApp(clingo.ClingoApp):
    def __init__(self, name):
        self.program_name = name

    def main(self, control, files):
        control.load("sudoku.lp")
        for f in files:
            control.load(f)
        control.ground([("base", [])])
        control.solve()

    def print_model(self, model):
        # Question 4: Use the __str__ method from Sudoku class
        sudoku_obj = Sudoku.from_model(model)
        print(sudoku_obj)

if __name__ == "__main__":
    clingo.clingo_main(SudokuApp(sys.argv[0]), sys.argv[1:])
