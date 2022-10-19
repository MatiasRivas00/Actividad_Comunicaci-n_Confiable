import sys
import SocketTCP
import time

_, ip, port = sys.argv
message = ''.join(sys.stdin.readlines())
  
# client
client_socketTCP = SocketTCP.SocketTCP()
client_socketTCP.connect((ip, int(port)))
start_time = time.time()
number_of_sent_messages = client_socketTCP.send(message, mode=2)
end_time = time.time()
print(f"TOTAL OF SENT MESSAGES: {number_of_sent_messages}", end='\n')
print(f"TOTAL TIME: {end_time - start_time}", end='\n\n\n')
client_socketTCP.close()
