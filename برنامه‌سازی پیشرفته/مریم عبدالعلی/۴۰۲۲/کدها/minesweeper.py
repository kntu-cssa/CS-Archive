# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:35:22 2024

@author: Maryam Abdolali
"""
import tkinter as tk
import random 
from tkinter import messagebox

class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.root = tk.Tk()
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.create_board()
        self.place_mines()
        
    def create_board(self):
        #self.buttons = [[None for i in range(self.cols)] for j in range(self.rows)]
        self.buttons = []
        for i in range(self.rows):
            button_row = []
            for j in range(self.cols):
                button = tk.Button(self.root, text ="", width=4, height=2)
                button.grid(row=i, column = j)
                button.bind("<Button-1>",self.left_click(i,j)) #lambda event, row=i, col=j: self.left_click(row,col)
                button.bind("<Button-3>",self.right_click(i,j)) #lambda event, row=i, col=j: self.right_click(row,col)
                button.mine = False
                button.revealed = False
                button.flagged = False
                button_row.append(button)
            self.buttons.append(button_row)
    def place_mines(self):
        ''' With list comprehension:
        self.mine_positions = random.sample([(r,c) for r in range(self.rows) for j in range(self.cols)], self.num_mines)
        for r, c in self.mine_positions:
            self.buttons[r][c].mine = True
        '''
        placed_mines = 0
        self.mine_positions = []
        while placed_mines < self.num_mines:
            r,c = random.randint(0, self.rows-1), random.randint(0, self.cols-1)
            if not self.buttons[r][c].mine:
                self.buttons[r][c].mine = True
                placed_mines += 1
                self.mine_positions.append((r,c))
                
            
        
    def left_click(self,i,j):
        def inner(event):
            button = self.buttons[i][j]
            if not button.revealed and not button.flagged:
                if button.mine:
                    self.reveal_mines()
                    messagebox.showinfo("Minesweeper", "Game over! You lost!")
                    self.root.destroy()
                else:
                    mine_count = self.local_mine_count(i,j)
                    button.config(text=str(mine_count) if mine_count > 0 else "", state=tk.DISABLED, relief=tk.SUNKEN, fg="black")
                    button.revealed= True
                    if mine_count == 0:
                        self.reveal_empty_cells(i,j)
                if self.is_winner():
                    messagebox.showinfo("Minesweeper", "You won!")
                    self.root.destroy()
        return inner
                
    def right_click(self,i,j):
        def inner(event):
            button = self.buttons[i][j]
            if not button.revealed:
                if not button.flagged:
                    button.config(text="🚩", fg="red")
                    button.flagged=True
                else:
                    button.config(text="", fg="black")
                    button.flagged=False
        return inner
    def reveal_empty_cells(self, row, col):
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if 0 <= i < self.rows and 0 <= j <self.cols:
                    if not self.buttons[i][j].mine and not self.buttons[i][j].revealed:
                        self.left_click(i, j)(None)
        
    def local_mine_count(self, row, col):
        count = 0
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if 0 <= i < self.rows and 0 <= j <self.cols:
                    count += int(self.buttons[i][j].mine)
        return count
    def reveal_mines(self):
        for r,c in self.mine_positions:
            self.buttons[r][c].config(text="💣", state=tk.DISABLED, relief=tk.SUNKEN, fg="black")
            
    def is_winner(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.buttons[i][j].revealed and not self.buttons[i][j].mine:
                    return False
        return True
    def start(self):
        self.root.mainloop()
                
game = Minesweeper(8, 8, 10)
game.start()
        