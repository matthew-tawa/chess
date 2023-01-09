import Constants
import socket
import sys


class Server():
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.game_loop()
        

    def game_loop(self):
        print('Starting server on %s port %s.' % (self.ip, self.port))
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)

        # find connections
        connection, client_address = self.sock.accept()
        print('Client with address %s connected.' % client_address)


        while True:
            try:
                message = connection.recv(999).decode()
                print(message)

                if message == 'quit':
                    break

            except:
                connection.close()

        print('Connection closed.')
        connection.close()
        self.sock.close()







