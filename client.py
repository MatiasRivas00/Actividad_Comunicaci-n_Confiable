import sys
import SocketTCP

_, ip, port = sys.argv
message = ''.join(sys.stdin.readlines())
  
# client
client_socketTCP = SocketTCP.SocketTCP()
client_socketTCP.connect((ip, int(port)))
client_socketTCP.send(message)
client_socketTCP.close()
