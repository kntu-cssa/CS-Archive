import tkinter as tk
import random

class CGame:
    
    colorList = ["Red", "Orange", "White", "Black",
                      "Green", "Blue", "Brown", "Purple",
                      "Cyan", "Yellow", "Pink", "Magenta"]
    def __init__(self, root):
        self.root = root
        self.root.title("Color Game")
        self.chosenColor = ""
        self.score = 0
        self.timer = 60
        self.createGUI(root)
 
        
    def createGUI(self,root):
        intro = tk.Label(root, text="Enter the color of the words displayed below", font=('Arial', 20))
        intro.grid(row=0,column=0,columnspan=3)
        
        self.score_label = tk.Label(root, text=("Your score is:" + str(self.score)),fg="blue",font = ('Arial', 20))
        self.score_label.grid(row=1,column=1)
        
        self.color_display = tk.Label(root, text ="", font=('Arial', 20))
        self.color_display.grid(row=2,column=1)
        
        self.time_left = tk.Label(root, text= ("Game ends in: -"),font = ('Arial', 20), fg = "red")
        self.time_left.grid(row=3, column =1)
        
        self.color_entry = tk.Entry(root, width = 30, font =('Arial', 20))
        self.color_entry.grid(row=4,column=1,pady=30,padx=10)
        self.color_entry.bind('<Return>',self.wordEntered)
        
        self.start_button = tk.Button(root, text="Start", width = 20, font = ('Arial', 20), bg = "light blue", command = self.startGame)
        self.start_button.grid(row=5, column =1)

        self.reset_button = tk.Button(root, text="Reset", width = 20, font = ('Arial', 20), bg = "pink", command = self.resetGame)
        self.reset_button.grid(row=6, column =1)
        
    def startGame(self):
        if self.timer == 60:
            self.chosenColor = random.choice(CGame.colorList)
            self.color_display.config(text=random.choice(CGame.colorList),fg=self.chosenColor)
            self.countDown()
    def countDown(self):
        if self.timer > 0:
            self.timer -= 1
            self.time_left.config(text= ("Game ends in: "+ str(self.timer)))
            self.after_id = self.time_left.after(1000,self.countDown)
            if self.timer == -1:
               self.time_left.config(text= "Game Over") 
               
    def resetGame(self):
        self.timer = 60
        self.score = 0
        self.chosenColor = ""
        self.color_display.config(text=self.chosenColor)
        self.score_label.config(text="Your score is: 0")
        self.time_left.config(text="Game ends in: -")
        self.color_entry.delete(0,tk.END)
        self.time_left.after_cancel(self.after_id)
        
    def wordEntered(self,event):
        if self.timer > 0:
            entered_color = self.color_entry.get().lower()
            if entered_color == self.chosenColor.lower():
                self.score += 1
                self.score_label.config(text=("Your score is: "+str(self.score)))
            self.chosenColor = random.choice(CGame.colorList)
            self.color_display.config(text=random.choice(CGame.colorList),fg=self.chosenColor)
            self.color_entry.delete(0,tk.END)
        
        
root = tk.Tk()
app = CGame(root)
root.mainloop()