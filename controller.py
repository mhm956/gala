# Server tutorial: https://pymotw.com/2/socket/tcp.html
from __future__ import print_function

import os
import sys
import json
import socket

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


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print('starting up on %s port %s', server_address)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from %s', client_address)
            while True:
                data = connection.recv(1024)
                if data:
                    user_message = data

                    if user_message == u"exit":
                        break

                    request = ai.text_request()
                    request.query = user_message

                    response = json.loads(request.getresponse().read())

                    result = response['result']
                    action = result.get('action')
                    actionIncomplete = result.get('actionIncomplete', False)

                    print(u"<--> %s" % response['result']['fulfillment']['speech'])

                else:
                    break
        finally:
            # Clean up the connection
            connection.close()


if __name__ == '__main__':
    main()
