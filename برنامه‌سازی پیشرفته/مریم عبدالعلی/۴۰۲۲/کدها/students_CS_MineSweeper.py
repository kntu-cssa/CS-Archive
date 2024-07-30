import tkinter as tk
import random
from tkinter import messagebox


class mind:
    def __init__(self,row,col,num_mines):
        self.root=tk.Tk()
        self.row=row
        self.col=col
        self.num_mines=num_mines
        self.creat_board()
        self.place_mines()
    def creat_board(self):
        self.buttons=[]
        
        for i in range(self.row):
            row_button=[]
            for j in range(self.col):
                b=tk.Button(self.root,text=' ', width=4, height=2)
                b.grid(row=i,column=j)
                b.bind("<Button-1>",self.left_click(i,j))
                b.bind("<Button-3>",self.right_click(i,j))
                b.mine=False
                b.flag=False
                b.revealed=False
                row_button.append(b)
            self.buttons.append(row_button)
    def left_click(self,i,j):
        def inner(event):
            b=self.buttons[i][j]
            if not b.revealed and not b.flag:
                if b.mine:
                    for r in range(self.row):
                        for c in range(self.col):
                            if self.buttons[r][c].mine:
                                self.buttons[r][c].config(text="💣",state=tk.DISABLED , relief=tk.SUNKEN)
                    messagebox.showinfo(' ','you lost')
                    self.root.destroy()
                else:
                    mine_count = self.local_mine_count(i, j)
                    self.buttons[i][j].revealed = True
                    if mine_count== 0 :
                        self.buttons[i][j].config(text = "" , state=tk.DISABLED , relief=tk.SUNKEN)
                        self.reveal_empty_cells(i,j)
                        
                    else:
                        self.buttons[i][j].config(text = f"{mine_count}" , state=tk.DISABLED, relief=tk.SUNKEN)
                    if self.is_winner():
                        messagebox.showinfo("MineSweeper", "You win")
                        self.root.destroy()
                        
                        
        return inner
    def right_click(self , i , j):
        def inner(event):
            if not self.buttons[i][j].revealed :
                if self.buttons[i][j].flag:
                    self.buttons[i][j].config(text ="")
                else:
                    self.buttons[i][j].config(text = "🚩")
        return inner
    def place_mines(self):
        cnt=0
        while cnt<self.num_mines:
            a,b=random.randint(0, self.row-1),random.randint(0, self.col-1)
            if not self.buttons[a][b].mine:
                self.buttons[a][b].mine=True
                cnt+=1
    def local_mine_count(self , i , j):
        cnt =0
        for r in range(i-1 , i+2):
            for c in range(j-1 , j+2):
                if 0<=r<self.row and 0<=c<self.col:
                    if self.buttons[r][c].mine:
                      cnt +=1
        return cnt
       
    def reveal_empty_cells(self , i , j):
        for r in range(i-1 , i+2):
            for c in range(j-1 , j+2):
                if 0<=r<self.row and 0<=c<self.col and not self.buttons[r][c].mine and not self.buttons[r][c].revealed:
                    self.left_click(r, c)(None)
    def play(self):
        self.root.mainloop()
    def is_winner(self):
        for i in range(self.row):
            for j in range(self.col):
                if not self.buttons[i][j].revealed and not self.buttons[i][j].mine:
                    return False
        return True
m1 = mind(8, 8, 5)
m1.play()
                