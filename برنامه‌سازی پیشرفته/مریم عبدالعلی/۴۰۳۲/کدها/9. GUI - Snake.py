import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root, width = 500, height = 500):
        self.root = root
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="black")
        self.canvas.pack()
        self.root.bind('<KeyPress>', self.changeDirection)
        self.cell_size = 20
        self.snake = [(200,200),(200,200+self.cell_size)]
        self.direction = 'Up'
        self.game_over = False
        self.food = self.insert_food()
        self.move()
    def changeDirection(self, event):
        if event.keysym in ["Up","Down", "Left", "Right"]:
            self.direction = event.keysym
    def move(self):
        if not self.game_over: 
            head_x, head_y = self.snake[0]
            if self.direction == 'Up':
                new_head = (head_x, head_y - self.cell_size)
            elif self.direction == 'Down':
                new_head = (head_x, head_y + self.cell_size)
            elif self.direction == 'Left':
                new_head = (head_x -self.cell_size , head_y)
            else:
                new_head = (head_x + self.cell_size, head_y)
            if not self.is_game_over(new_head):
                self.snake.insert(0,new_head)
                if new_head[0]==self.food[0] and new_head[1]==self.food[1]:
                    self.food = self.insert_food()
                else:
                    self.snake.pop()
                self.draw()
                self.root.after(500, self.move)
            else:
                self.canvas.create_text(self.width//2, self.height//2, text="Game Over", fill="white", font=('Arial', 20))
                self.game_over = True
    def is_game_over(self, new_head):
        if new_head[0]<0 or new_head[1] <0 or new_head[0]>=self.width or new_head[1]>=self.height:
            return True
        if new_head in self.snake:
            return True
        return False

    def insert_food(self):
        new_x = random.randint(0, self.width//self.cell_size)*self.cell_size
        new_y = random.randint(0, self.height//self.cell_size)*self.cell_size
        return (new_x, new_y)
    def eat_food(self):
        pass
    def draw(self):
        self.canvas.delete("all")
        for item in self.snake:
            self.canvas.create_rectangle(item[0],item[1],item[0]+self.cell_size, item[1]+self.cell_size, fill='green')
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0]+self.cell_size, self.food[1]+self.cell_size, fill="red")

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()


    