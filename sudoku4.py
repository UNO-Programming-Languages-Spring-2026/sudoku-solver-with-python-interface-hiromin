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
        res = []

        board = {}
        for symbol in model.symbols(shown=True):
            if symbol.name == "sudoku" and len(symbol.arguments) == 3:
                # Extract arguments as integers
                r = symbol.arguments[0].number
                c = symbol.arguments[1].number
                v = symbol.arguments[2].number
                board[(r, c)] = v
        
        for r in range(1, 10):
            row_str = ""
            for c in range(1, 10):
                val = str(board[(r, c)] if (r, c) in board else "-")
                row_str += val
                if c == 9:
                    continue
                elif c % 3 == 0:
                    row_str += "  "  # Two spaces between blocks
                else:
                    row_str += " "   # One space between cells
            res.append(row_str)
            if r % 3 == 0 and r < 9:
                res.append("") # Empty line between blocks
        print("\n".join(res))

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())
    