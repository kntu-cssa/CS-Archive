import tkinter as tk 
from tkinter import messagebox

class Player:
    def __init__(self, symbol, color):
        self.symbol = symbol
        self.color = color
        
class Board:
    def __init__(self):
        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        
    def is_winner(self):
        for i in range(3):
            if self.cells[i][0] == self.cells[i][1] == self.cells[i][2] != ' ':
                return True
            if self.cells[0][i] == self.cells[1][i] == self.cells[2][i] != ' ':
                return True
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != ' ':
            return True
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] != ' ':
            return True
        return False
    
    def is_draw(self):
        for row in range(3):
            for col in range(3):
                if self.cells[row][col] == ' ':
                    return False
        return True
    
class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TicTacToe")
        self.players = [Player("X","red"), Player("O","blue")]
        self.current_player = self.players[0]
        self.board = Board()
        self.buttons = [[None, None, None],[None, None, None], [None, None, None]]
        self.createButtons()
        
    def createButtons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=' ', font=('Arial', 20), width=5, height=2, command = self.on_click(i,j))
                self.buttons[i][j].grid(row = i, column = j)
                
    def on_click(self,i,j):
        def inner():
            if self.board.cells[i][j] == ' ':
                self.board.cells[i][j] = self.current_player.symbol
                self.buttons[i][j].config(text=self.current_player.symbol, fg=self.current_player.color)
                if self.board.is_winner():
                    messagebox.showinfo("TicTacToe", f"{self.current_player.symbol} has won")
                    self.root.destroy()
                elif self.board.is_draw():
                    messagebox.showinfo("TicTacToe", "The game is a tie!")
                    self.root.destroy()
                else:
                    self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
        return inner
    def play(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()