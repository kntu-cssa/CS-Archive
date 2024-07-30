import matplotlib.pyplot as plt
import generate


class Maz_solver:
    def __init__(self, height, width, maze):
        self.height = height
        self.width = width
        self.maze = maze
        self.path = []

    def DFS(self,x=0,y=0,sol=[(0,0)],vis=[]):
        vis.append((x,y))
        if x==self.height-1 and y==self.width-1:
            self.path=sol
            return True
        if x-1>=0 and self.maze[x-1][y]!=0 and (x-1,y) not in vis:
            sol.append((x-1,y))
            if self.DFS(x-1,y,sol,vis):
                return True
            sol.pop()
        if x+1<self.height and self.maze[x+1][y] and (x+1,y) not in vis:
            sol.append((x+1,y))
            if self.DFS(x+1,y,sol,vis):
                return True
            sol.pop()
        if y-1>=0 and self.maze[x][y-1] and (x,y-1) not in vis:
            sol.append((x,y-1))
            if self.DFS(x,y-1,sol,vis):
                return True
            sol.pop()
        if y+1<self.width and self.maze[x][y+1] and (x,y+1) not in vis:
            sol.append((x,y+1))
            if self.DFS(x,y+1,sol,vis):
                return True
            sol.pop()
        return False
        
    
    def print_path(self):
        print(self.path)
        for x,y in self.path:
            self.maze[x][y]=0.5
        plt.imshow(self.maze, cmap="gray")
        plt.show()

if __name__ == '__main__':
    N=M=21
    maze_1 = generate.generate_maze(N, M)
    my_maz = Maz_solver(M,N,maze_1)
    if (my_maz.DFS()):
        print("Path Found!")
        my_maz.print_path()
    else:
        print("No Path Found!")