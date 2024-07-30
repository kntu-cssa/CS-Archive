from random import shuffle

def generate_maze(w, h):
    maze = [[0]*w for i in range(h)]
    dir = [(0,1), (1,0), (-1,0), (0,-1)]
    def backtrack(x = 0, y = 0):
        maze[x][y] = 1
        choices = [ i for i in range(4) if 0 <= dir[i][0]*2 + x < h and 0 <= dir[i][1]*2 + y < w]   
        shuffle(choices)
        for t in choices:
            if maze[dir[t][0]*2 + x][dir[t][1]*2 + y] == 0:
                maze[dir[t][0] + x][dir[t][1] + y] = 1
                backtrack(dir[t][0]*2 + x, dir[t][1]*2 + y)
    backtrack()
    return maze

