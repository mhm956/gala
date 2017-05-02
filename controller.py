from __future__ import print_function

import os
import sys
import json
from socket import socket

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

    import apiai

# personal agent access token: 470a48429715494cbb1cf8c6080bf0e6
CLIENT_ACCESS_TOKEN = '470a48429715494cbb1cf8c6080bf0e6'

sock = socket()
sock.connect(('localhost', 5987))


def readlines(sock, recv_buffer=1024, delim='\n'):
    buffering = ''
    data = True
    while data:
        data = sock.recv(recv_buffer)
        buffering += data

        while buffering.find(delim) != -1:
            line, buffering = buffering.split('\n', 1)
            yield line
    return


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    while True:
        # print(u"--> ", end=u"")
        # TODO plug in client here
        # user_message = raw_input()
        for line in readlines(sock):
            user_message = line

            if user_message == u"exit":
                break

            request = ai.text_request()
            request.query = user_message

            response = json.loads(request.getresponse().read())

            result = response['result']
            action = result.get('action')
            actionIncomplete = result.get('actionIncomplete', False)

            print(u"<--> %s" % response['result']['fulfillment']['speech'])


if __name__ == '__main__':
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)
    print('Going to forever')
    server.serve_forever()
    print('Going to main')
    main()
