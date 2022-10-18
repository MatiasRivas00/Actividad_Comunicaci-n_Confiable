import SocketTCP

for i in range(5):
    # server 
    server_socketTCP = SocketTCP.SocketTCP()
    server_socketTCP.bind(('localhost', 8000))
    complete_message = b''
    encoded_message = b''

    while True:
        connection_socketTCP, new_address = server_socketTCP.accept()
        while encoded_message is not None:
            complete_message += encoded_message
            encoded_message = connection_socketTCP.recv(16, mode=0)

        print(complete_message.decode())
        break
    server_socketTCP.close()