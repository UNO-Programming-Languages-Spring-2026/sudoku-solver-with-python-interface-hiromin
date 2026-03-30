import sys
import clingo


class ClingoApp(clingo.application.Application):

    def main(self, ctl, files):
        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.ground([("base", [])])
        ctl.solve(on_model=self.print_model)

    def print_model(self, model):
        symbols = sorted(model.symbols(shown=True))
        print(" ".join(str(s) for s in symbols))
        sys.stdout.flush()


# REQUIRED for Python ↔ ASP interface
class Context:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def initial(self):
        facts = []

        for (i, j), v in self.sudoku.sudoku.items():
            facts.append(
                clingo.Function(
                    "initial",
                    [clingo.Number(i), clingo.Number(j), clingo.Number(v)]
                )
            )

        return facts


clingo.application.clingo_main(ClingoApp())
