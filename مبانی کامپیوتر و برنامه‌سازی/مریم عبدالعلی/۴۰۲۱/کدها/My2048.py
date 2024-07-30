import random

def main():
    gameBoard = getNewBoard()
    while True:
        displayBoard(gameBoard)
        move = getPlayerMove()
        if move == 'Q':
            return
        makeMove(gameBoard, move)
        addTwo(gameBoard)
        score = getScore(gameBoard)
        if isFull(gameBoard):
            displayBoard(gameBoard)
            print("Game over!")
            print(f"Your score is {score}!")
            break
        
        
def getNewBoard():
    board = [[0]*4 for i in range(4)]    
    num = 0
    while num < 2:
        posi, posj = random.randint(0,3), random.randint(0,3)
        if board[posi][posj] == 0:
            board[posi][posj] = 2
            num += 1
    return board

def displayBoard(board):
    vals = []
    for i in range(4):
        for j in range(4):
            val = board[i][j]
            if val==0:
                val = ''
            vals.append(str(val).center(5))
    strBoard = f'''
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{vals[0]}|{vals[1]}|{vals[2]}|{vals[3]}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{vals[4]}|{vals[5]}|{vals[6]}|{vals[7]}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{vals[8]}|{vals[9]}|{vals[10]}|{vals[11]}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{vals[12]}|{vals[13]}|{vals[14]}|{vals[15]}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    '''
    print(strBoard)
    
def getPlayerMove():
    print('Enter move: (WASD or Q to quit)')
    while True:
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D', 'Q'):
            return move
        print('Enter one of "W", "A", "S", "D", or "Q".')
        
def makeMove(board, move):
    if move == "A":
        for i in range(4):
            tile = [board[i][0], board[i][1], board[i][2], board[i][3]]
            board[i] = combine(tile)
    elif move == "D":
        for i in range(4):
            tile = [board[i][3], board[i][2], board[i][1], board[i][0]]
            board[i][3], board[i][2], board[i][1], board[i][0] = combine(tile)
    elif move == "W":
        for i in range(4):
            tile = [board[0][i], board[1][i], board[2][i], board[3][i]]
            board[0][i], board[1][i], board[2][i], board[3][i] = combine(tile)
    elif move == "S":
        for i in range(4):
            tile = [board[3][i], board[2][i], board[1][i], board[0][i]]
            board[3][i], board[2][i], board[1][i], board[0][i] = combine(tile)
            
def combine(seq):
    combinedTiles = []
    for i in range(4):
        if seq[i] != 0:
            combinedTiles.append(seq[i])
    while len(combinedTiles) < 4:
        combinedTiles.append(0)
        
    for i in range(3):
        if combinedTiles[i] == combinedTiles[i+1]:
            combinedTiles[i] *= 2
            combinedTiles[i+1:-1] = combinedTiles[i+2:]
            combinedTiles[-1] = 0
    return combinedTiles

def addTwo(board):
    while True:
        posi,posj = random.randint(0,3), random.randint(0,3)
        if board[posi][posj]==0:
            board[posi][posj]=2
            break
            
def getScore(board):
    s = 0
    for i in range(4):
        for j in range(4):
            s += board[i][j]
    return s

def isFull(board):
    for i in range(4):
        for j in range(4):
            if board[i][j]==0:
                return False
    return True

if __name__=="__main__":
    main()