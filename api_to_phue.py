#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python Example that sends commands to remote hosted API.AI client.
The client returns an appropriate response if the 
"""
from __future__ import print_function

from time import sleep
import os
import sys
import json

from Phillips.smart_lights import phue_lights

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

    while True:
        print(u"> ", end=u"")
        user_message = raw_input()

        if user_message == u"exit":
            break

        request = ai.text_request()
        request.query = user_message

        response = json.loads(request.getresponse().read())

        result = response['result']
        action = result.get('action')

        actionIncomplete = result.get('actionIncomplete', False)

        print(u"< %s" % response['result']['fulfillment']['speech'])

        if action is not None:
            parameters = result['parameters']

            if action == u"smart-light-action":
                color = parameters['color']
                light_state = parameters['light_state']
                room = parameters['room']
                light_result = phue_lights(color, light_state, room)
                sleep(2)  # Let GALA finish talking
                if light_result:
                    print("ok, all done!")
                else:
                    print("sorry, couldn't set the lights")

if __name__ == '__main__':
    main()
