from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")

    def play(self):
        current = self.player1
        while True:
            self.board.display()
            row, col = current.get_move()
            if self.board.update(row, col, current.mark):
                if self.board.is_winner(current.mark):
                    self.board.display()
                    print(f"{current.name} ({current.mark}) wins!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a tie!")
                    break
                current = self.player2 if current == self.player1 else self.player1
            else:
                print("That spot is already taken. Try again.")
