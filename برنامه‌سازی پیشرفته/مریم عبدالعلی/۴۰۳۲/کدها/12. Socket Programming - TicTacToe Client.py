import tkinter as tk
import socket
import threading
from tkinter import messagebox 

class TicTacToeClient:
    def __init__(self, host="127.0.0.1", port=8000):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.symbol = None
        self.board = ["" for i in range(9)]
        self.turn = False
        self.create_GUI()

    def create_GUI(self):
        self.root = tk.Tk()
        self.root.title("TicTacToe")
        self.buttons = [tk.Button(self.root, text="", width=20, height=10, command=lambda i=i: self.make_move(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)
        self.status_label = tk.Label(self.root, text="Waiting for game to start...", font=("Arial", 14))
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.thread = threading.Thread(target=self.recv_msg)
        self.thread.start()
        self.root.mainloop()
    def recv_msg(self):
        while True:
            try:
                msg = self.client.recv(1024).decode("utf-8")
                print(msg)
                if "You are Player" in msg:
                    self.symbol = msg.split()[-1]
                    self.status_label.config(text=f"You are {self.symbol}")
                elif "Board" in msg:
                    board_txt = msg.split("\n")[-1]
                    self.board = eval(board_txt)
                    for i in range(9):
                        self.buttons[i].config(text=self.board[i])
                elif "Your Move" in msg:
                    self.turn = True
                    self.status_label.config(text="Your Turn!")
                elif "opponent..." in msg:
                    self.status_label.config(text="Opponent's turn...")

                elif "Game over!" in msg:
                    messagebox.showinfo("Game Over", msg)
                    self.root.quit()
                    break
            except:
                break
    def make_move(self, index):
        if not self.turn:
            self.status_label.config(text="Your opponent turn...")
            return
        if self.board[index] == "" and self.symbol:
            print("sent", index+1)
            self.client.send(str(index + 1).encode("utf-8"))
            self.turn = False
        else: 
            self.status_label.config(text="Invalid Move")

TicTacToeClient()