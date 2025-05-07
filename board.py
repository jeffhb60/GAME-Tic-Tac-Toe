class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.grid:
            print("|".join(row))
            print("-" * 5)

    def update(self, row, col, mark):
        if self.grid[row][col] == " ":
            self.grid[row][col] = mark
            return True
        return False

    def is_winner(self, mark):
        # Rows, Columns, Diagonals
        for i in range(3):
            if all(self.grid[i][j] == mark for j in range(3)) or \
               all(self.grid[j][i] == mark for j in range(3)):
                return True
        return (all(self.grid[i][i] == mark for i in range(3)) or
                all(self.grid[i][2 - i] == mark for i in range(3)))

    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)