import Constants
import socket
import sys

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (Constants.SERVER_ADDRESS, Constants.SERVER_PORT)

sock.connect(server_address)

print('Connecting to %s port %s' % server_address)

while True:
    try:
        message = input('Message: ')
        sock.sendall(message.encode())

        if message == 'quit':
            break

    except Exception as e:
        print(e)
        break

sock.close()




