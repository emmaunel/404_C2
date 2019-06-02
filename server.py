import socket
import sys


host = '10.1.1.84'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

try:
    s.bind((host, port))
except socket.error as err:
    print("Error occured: ", err)
    sys.exit()

s.listen(10)
print("Socket is listening....")

while True:
    print("Waiting for connection")
    client, address = s.accept()
    print("Connected from ...", address)
