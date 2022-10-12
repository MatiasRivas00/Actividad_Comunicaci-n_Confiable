import SocketTCP

# server 
server_socketTCP = SocketTCP.SocketTCP()
server_socketTCP.bind(('localhost', 8000))
complete_message = b''
encoded_message = b''

while True:
    connection_socketTCP, new_address = server_socketTCP.accept()
    while encoded_message is not None:
        complete_message += encoded_message
        encoded_message = connection_socketTCP.recv(16, mode=1)

    print(complete_message.decode())
    