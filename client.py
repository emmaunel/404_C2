"""
Client
"""
import os
import requests

class Client:
    def __init__(self):
        self.url = 'http://172.16.58.166/error.html'
        self.os = os.name

    def os(self):
        print("I am currently " + str(self.os))

    # def attack(self):


cli = Client()
while True:
    error_page = ''
    try:
        requests.get(cli.url)
    except requests.HTTPError as err:
        print(err)