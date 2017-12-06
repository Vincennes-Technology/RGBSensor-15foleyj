#Josie
import socket
import time
SERVERIP = '10.0.0.22'
n = 0
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVERIP, 8881))
    print "%d : Connected to server \n"
    data = "Josie's RGB sensor has detected a new color "%d
    print " Sent:", data
    sock.close()
    n += 1
    time.sleep(10)
