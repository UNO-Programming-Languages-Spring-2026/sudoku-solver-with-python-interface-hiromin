import sys
import clingo
from sudoku_board import Sudoku

class Context:
    def __init__(self, board: Sudoku):
        self.sudoku = board

    def initial(self) -> list[clingo.symbol.Symbol]:
        facts = []
        for (r, c), v in self.sudoku.board.items():
            facts.append(clingo.Function("", [clingo.Number(r), clingo.Number(c), clingo.Number(v)]))
        return facts

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        with open(files[0], 'r') as f:
            content = f.read()
        
        sudoku_instance = Sudoku.from_str(content)
        ctx = Context(sudoku_instance)

        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")

        ctl.ground([("base", [])], context=ctx)
        ctl.solve()

    def print_model(self, model, printer):
        print(Sudoku.from_model(model))

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())