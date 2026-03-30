import sys
import clingo

class SudokuApp(clingo.ClingoApp):
    def __init__(self, name):
        self.program_name = name

    def main(self, control, files):
        # Load the base sudoku logic and the instance files
        control.load("sudoku.lp")
        for f in files:
            control.load(f)
        control.ground([("base", [])])
        control.solve()

    # Question 1b: Overwrite print_model to sort alphabetically
    def print_model(self, model):
        symbols = model.symbols(shown=True)
        sorted_symbols = sorted(symbols, key=lambda s: str(s))
        print(" ".join(map(str, sorted_symbols)))

if __name__ == "__main__":
    clingo.clingo_main(SudokuApp(sys.argv[0]), sys.argv[1:])
