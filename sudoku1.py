import sys, clingo

class ClingoApp(clingo.application.Application):

    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground()
        ctl.solve()

    def print_model(self, model, printer):
        # Sort symbols alphabetically by their string representation
        parts = [str(sym) for sym in model.symbols(shown=True)]
        parts.sort()
        print(" ".join(parts))

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
        # Sort symbols alphabetically by their string representation
        parts = [str(sym) for sym in model.symbols(shown=True)]
        parts.sort()
        print(" ".join(parts))

if __name__ == "__main__":
    clingo.clingo_main(SudokuApp(sys.argv[0]), sys.argv[1:])
    clingo.application.clingo_main(ClingoApp())
    