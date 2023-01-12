import socket
import Chess
import Constants


class Client():
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # chess game
        self.chess = Chess.Chess(Constants.Color.DARK)

    # connects to server
    def join_server(self):
        print('Connecting to %s port %s' % (self.ip, self.port))
        self.sock.connect((self.ip, self.port))

    # runs the game
    def game_loop(self):
        while True:
            try:
                opp_move = self.sock.recv(1024).decode()

                my_move = self.chess.myturn()

                self.sock.sendall(my_move.encode())

                if message == 'quit':
                    break

            except Exception as e:
                print(e)
                break

        print('Connection closed.')
        self.sock.close()








