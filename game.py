from tkinter import messagebox

from player import Player as GUIPlayer
import tkinter as tk

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.board = Board()
        self.player1 = GUIPlayer("Player 1", "X")
        self.player2 = GUIPlayer("Player 2", "O")
        self.current_player = self.player1

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text=" ", font=('Arial', 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def handle_click(self, row, col):
        if self.board.grid[row][col] == " ":
            self.board.update(row, col, self.current_player.mark)
            self.buttons[row][col]['text'] = self.current_player.mark
            if self.board.is_winner(self.current_player.mark):
                messagebox.showinfo("Game Over", f"{self.current_player.name} ({self.current_player.mark}) wins!")
                self.window.quit()
            elif self.board.is_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.window.quit()
            else:
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        else:
            messagebox.showwarning("Invalid Move", "That spot is already taken.")

    def run(self):
        self.window.mainloop()
