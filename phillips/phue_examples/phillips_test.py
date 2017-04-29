"""
Python Test to Confirm Phillips Hue Bridge Connection
"""
# Based on example: https://github.com/studioimaginaire/phue

from phue import Bridge
from time import sleep
import logging
logging.basicConfig()


def lamp_check():

    print "The following lights have been found"
    lights = b.get_light_objects('id')
    for light in lights:
        print "---> " + "ID# " + str(light) + ": " + lights[light].name

if __name__ == '__main__':
    # Will need to change bridge when renewed IP by DNS
    b = Bridge('192.168.0.103')
    b.connect()
    b.get_api()
    lamp_check()
