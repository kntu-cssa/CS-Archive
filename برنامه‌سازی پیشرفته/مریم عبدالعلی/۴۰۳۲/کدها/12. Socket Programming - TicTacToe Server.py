import socket
import threading

class TicTacToeServer:
    def __init__(self,host="127.0.0.1", port=8000):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host,port))
        self.server.listen(2) # Two players max
        self.players = {} # Stores connected player sockets {'X': socket1, 'O': socket2}
        self.current_player =  'X'
        self.board = ["" for i in range(9)]
    def start(self):
        while len(self.players) < 2:
            client_socket, addr = self.server.accept()
            symbol = "X" if len(self.players) == 0 else "O"
            self.players[symbol] = client_socket
            print(f"Player {symbol} connected from {addr}")
            thread = threading.Thread(target=self.handle_client, args = (client_socket, symbol))
            thread.start()
    def handle_client(self, client_socket, symbol):
        client_socket.send(f"You are Player {symbol}".encode("utf-8"))
        while len(self.players)<2:
            pass # Wait for two players to connect
        try:
            while True:
                if symbol == self.current_player:
                    client_socket.send("Your Move!".encode("utf-8"))
                    move = client_socket.recv(1024).decode("utf-8").strip()
                    if not move.isdigit() or int(move) not in range(1,10) or self.board[int(move)-1]!="":
                        client_socket.send("invalid move! Try again".encode("utf-8"))
                    else:
                        self.board[int(move)-1]=symbol
                        winner = self.check_winner()
                        self.update_client_boards()
                        if winner:
                            if winner == "draw":
                                msg = "Game Over! It's a draw!"
                            else:
                                msg = f"Game over!\n {winner} won!"
                            for player in self.players.values():
                                player.send(msg.encode("utf-8"))
                            break
                        self.current_player = "X" if self.current_player == "O" else "O"
                        client_socket.send("waiting for opponent...".encode("utf-8"))

        except:
            client_socket.close()

    def update_client_boards(self):
        for player in self.players.values():
            player.send(f"Board:\n {self.board}".encode("utf-8"))
        
    def check_winner(self):
        win_patterns = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != " ":
                return self.board[a]  # 'X' or 'O'
        if " " not in self.board:
            return "draw"
        return None


    
TicTacToeServer().start()
