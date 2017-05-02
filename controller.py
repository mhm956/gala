from __future__ import print_function

import os
import sys
import json
import socketserver

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
data_string = ""


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        global data_string
        data_string = self.request.recv(1024).strip()
        # print("{} wrote:".format(self.client_address[0]))
        return self.data


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    while True:
        # print(u"--> ", end=u"")
        # TODO plug in client here
        # user_message = raw_input()
        user_message = data_string

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
