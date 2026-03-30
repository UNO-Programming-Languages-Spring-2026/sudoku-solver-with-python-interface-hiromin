import sys
import clingo

class SudokuApp(clingo.ClingoApp):
    def __init__(self, name):
        self.program_name = name

    def main(self, control, files):
        # Load core logic (provided in project) and instance files
        control.load("sudoku.lp")
        for f in files:
            control.load(f)
        control.ground([("base", [])])
        control.solve()

    def print_model(self, model):
        # Question 1b: Alphabetical sort for the autograder
        symbols = model.symbols(shown=True)
        sorted_symbols = sorted(symbols, key=lambda s: str(s))
        print(" ".join(map(str, sorted_symbols)))

if __name__ == "__main__":
    clingo.clingo_main(SudokuApp(sys.argv[0]), sys.argv[1:])
