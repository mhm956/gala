# Server tutorial: https://pymotw.com/2/socket/tcp.html
from __future__ import print_function

import json
import os
import socket
import sys
from time import sleep
from Phillips.smart_lights import phue_lights
from Google.gmaps import gmaps

from Amazon.polly import VoiceSynthesizer

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

voice_synth = VoiceSynthesizer()


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print('---> Starting up on', server_address[0], 'port', server_address[1])
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print('---> Waiting for a connection')
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
                    voice_synth.say(response['result']['fulfillment']['speech'])

                    if action is not None:
                        parameters = result['parameters']

                        if action == u"smart-light-action":
                            color = parameters['color']
                            light_state = parameters['light_state']
                            room = parameters['room']
                            light_result = phue_lights(color, light_state, room)
                            if light_result:
                                voice_synth.say("ok, all done!")
                                sleep(2)  # Let GALA finish talking
                            else:
                                voice_synth.say("sorry, couldn't set the lights")
                                sleep(2)  # Let GALA finish talking
                        elif action == u"travel-time":
                            location = parameters['location']
                            route_time = gmaps(location)
                            if route_time:
                                route_string = "Currently your route time to " + location + " with traffic is " + \
                                               route_time
                                voice_synth.say(route_string)
                                sleep(3)
                            else:
                                voice_synth.say("Sorry I couldn't find that route")
                                sleep(2)
                else:
                    break
        finally:
            # Clean up the connection
            connection.close()


if __name__ == '__main__':
    main()
