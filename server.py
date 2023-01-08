import constants
import socket
import sys

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (constants.SERVER_ADDRESS, constants.SERVER_PORT)

print('Starting server on %s port %s' % server_address)

sock.bind(server_address)
sock.listen(1)

# find connections
connection, client_address = sock.accept()

while True:
    try:
        message = connection.recv(999).decode()
        print(message)

        if message == 'quit':
            break

    except:
        connection.close()

connection.close()


