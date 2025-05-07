class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_move(self):
        while True:
            try:
                row = int(input(f"{self.name} ({self.mark}) enter row (0-2): "))
                col = int(input(f"{self.name} ({self.mark}) enter column (0-2): "))
                if row in range(3) and col in range(3):
                    return row, col
                print("Invalid input. Try 0-2.")
            except ValueError:
                print("Invalid input. Must be numbers.")