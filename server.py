import socket
import sys
from threading import Thread
from codecs import decode

host = '10.1.1.84'
port = 1234


class ClientHandler(Thread):
    def __init__(self, cli):
        Thread.__init__(self)
        self.client = cli

    def run(self):
        self.name = decode(self.client.recv(1024), 'ascii')
        self.client.close()


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
    handler = ClientHandler(client)
    handler.start()
