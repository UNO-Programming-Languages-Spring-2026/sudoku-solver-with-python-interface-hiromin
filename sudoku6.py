import sys
import clingo
from sudoku_board import Sudoku

class Context:
    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku

    def initial(self):
        # Generates initial(r, c, v) facts for Clingo
        facts = []
        for (r, c), v in self.sudoku.board.items():
            facts.append(clingo.Function("initial", [clingo.Number(r), clingo.Number(c), clingo.Number(v)]))
        return facts

class SudokuApp(clingo.ClingoApp):
    def __init__(self, name):
        self.program_name = name

    def main(self, control, files):
        # Read the .txt file content
        with open(files[0], 'r') as f:
            content = f.read()
        
        # Build context from the string
        sudoku_instance = Sudoku.from_str(content)
        ctx = Context(sudoku_instance)

        control.load("sudoku.lp")
        control.load("sudoku_py.lp")
        control.ground([("base", [])], context=ctx)
        control.solve()

    def print_model(self, model):
        print(Sudoku.from_model(model))

if __name__ == "__main__":
    clingo.clingo_main(SudokuApp(sys.argv[0]), sys.argv[1:])
