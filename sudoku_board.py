import clingo

class Sudoku:
    def __init__(self, board: dict):
        # board is a dict: {(row, col): value}
        self.board = board

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> 'Sudoku':
        board = {}
        for symbol in model.symbols(shown=True):
            if symbol.name == "sudoku" and len(symbol.arguments) == 3:
                r = symbol.arguments[0].number
                c = symbol.arguments[1].number
                v = symbol.arguments[2].number
                board[(r, c)] = v
        return cls(board)

    @classmethod
    def from_str(cls, s: str) -> 'Sudoku':
        board = {}
        # Filter out empty strings from extra spaces/newlines
        tokens = s.split()
        for idx, token in enumerate(tokens):
            if token != "-":
                row = (idx // 9) + 1
                col = (idx % 9) + 1
                board[(row, col)] = int(token)
        return cls(board)

    def __str__(self) -> str:
        lines = []
        for r in range(1, 10):
            row_parts = []
            for c in range(1, 10):
                val = str(self.board.get((r, c), "-"))
                row_parts.append(val)
                # Extra space between 3x3 blocks horizontally
                if c in [3, 6]:
                    row_parts.append("")
            
            lines.append(" ".join(row_parts).rstrip())
            # Empty line between 3x3 blocks vertically
            if r in [3, 6]:
                lines.append("")
        return "\n".join(lines)
