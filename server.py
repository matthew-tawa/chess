import Constants
import socket
import


class Server():
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # client info (to be populated on connection)
        self.conn = None
        self.addr = None

    # opens server and waits for a connection
    def start_server(self):
        print('Starting server on %s, port %s.' % (self.ip, self.port))
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)

        # find connections
        self.conn, self.addr = self.sock.accept()
        print('Client with address %s connected.' % self.addr)

    # runs the game
    def game_loop(self):
        while True:
            try:
                message = self.conn.recv(1024).decode()
                print(message)

                if message == 'quit':
                    break

            except Exception as e:
                print(e)
                break

        print('Connection closed.')
        self.conn.close()
        self.sock.close()







