"""
Client
"""
import os

class Client:
    def __init__(self):
        self.url = 'http://10.1.1.84/error.html'
        self.os = os.name

    def print(self):
        print("I am currently " + str(self.os))


cli = Client()
cli.print()