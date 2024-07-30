import tkinter as tk 
import random 
from tkinter import messagebox
class Minesweeper:
    def __init__(self,rows,columns,num_mines):
        self.rows=rows
        self.columns= columns
        self.num_mines = num_mines 
        self.window=tk.Tk()
        self.creat_board()
        self.place_mines()
    def creat_board(self):
        self.buttons=[]
        for i in range(self.rows):
            row_button=[]
            for j in range(self.columns):
                b=tk.Button(self.window,text=" ",width=4,height=2)
                b.grid(row=i,column=j)
                b.bind("<Button-1>",self.left_click(i,j))
                b.bind("<Button-3>",self.right_click(i,j))
                b.mine=False
                b.flagged=False
                b.revealed=False
                row_button.append(b)
            self.buttons.append(row_button)
    def left_click(self,i,j):
        def inner(event):
            b=self.buttons[i][j]
            if not b.flagged and not b.revealed:
                if b.mine:
                    for row in range(self.rows):
                        for col in range(self.columns):
                            if self.buttons[row][col].mine:
                                self.buttons[row][col].config(text="💣" ,relief= tk.SUNKEN,state=tk.DISABLED )
                    messagebox.showinfo("Minesweeper","you lost!")
                    self.window.destroy()
                else :
                    b.revealed = True
                    mines = self.local_mine_count(i, j)
                    if mines == 0 :
                        pass
                        self.reveal_empty_cells(i, j)
                        b.config(text=" ",relief= tk.SUNKEN, state=tk.DISABLED)
                    else:
                        b.config(text=str(mines),relief= tk.SUNKEN, state=tk.DISABLED) 
                if self.is_winner():
                    messagebox.showinfo("MineSweeper","YOU WONNN")
        return inner
    def local_mine_count(self, i, j):
        counter = 0
        for row in range(i-1,i+2):
            for col in range(j-1,j+2):
                if 0<= row < self.rows and 0 <= col < self.columns:
                    counter += int(self.buttons[row][col].mine)
        return counter
    
    def right_click(self,i,j):
        def inner(event):
            if not self.buttons[i][j].revealed:
                if self.buttons[i][j].flagged:
                    self.buttons[i][j].config(text=' ')
                    self.buttons[i][j].flagged = False
                else:
                    self.buttons[i][j].config(text="🚩")
                    self.buttons[i][j].flagged = True
        return inner
    def place_mines(self):
        counter=0
        while counter < self.num_mines:
            a,b=random.randint(0,self.rows-1) , random.randint(0,self.columns-1)
            if not self.buttons[a][b].mine:
                self.buttons[a][b].mine= True
                counter += 1

    def play(self):
        self.window.mainloop()
    def reveal_empty_cells(self, i , j):
        for row in range(i-1,i+2):
            for col in range(j-1,j+2):
                if 0<= row < self.rows and 0 <= col < self.columns:
                    if not self.buttons[row][col].revealed:
                        self.left_click(row, col)(None)
    def is_winner(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if not self.buttons[i][j].revealed and not self.buttons[i][j].mine:
                    return False
        return True
m1 = Minesweeper(8, 8, 5)
m1.play()        