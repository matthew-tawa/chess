import Constants
import socket
import sys


class Client():
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.game_loop()

    def game_loop(self):
        print('Connecting to %s port %s' % (self.ip, self.port))
        self.sock.connect((self.ip, self.port))

        while True:
            try:
                message = input('Message: ')
                self.sock.sendall(message.encode())

                if message == 'quit':
                    break

            except Exception as e:
                print(e)
                break

        print('Connection closed.')
        self.sock.close()








