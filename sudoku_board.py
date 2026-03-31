import clingo

class Sudoku:
    def __init__(self, board: dict):
        # Ensure keys are (int, int) and values are int
        self.board = board
        self.sudoku = board

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> 'Sudoku':
        board = {}
        for symbol in model.symbols(shown=True):
            if symbol.name == "sudoku" and len(symbol.arguments) == 3:
                # Extract arguments as integers
                r = symbol.arguments[0].number
                c = symbol.arguments[1].number
                v = symbol.arguments[2].number
                board[(r, c)] = v
        return cls(board)

    @classmethod
    def from_str(cls, s: str) -> 'Sudoku':
        board = {}
        # Split by any whitespace (newlines, tabs, spaces)
        tokens = s.split()
        for idx, token in enumerate(tokens):
            if token != "-":
                # idx 0-80 maps to rows 1-9 and cols 1-9
                row = (idx // 9) + 1
                col = (idx % 9) + 1
                board[(row, col)] = int(token)
        return cls(board)

    def __str__(self) -> str:
        res = []
        for r in range(1, 10):
            row_str = ""
            for c in range(1, 10):
                val = str(self.board.get((r, c), "-"))
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
        return "\n".join(res)
