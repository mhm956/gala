import googlemaps
from datetime import datetime

gmaps_request = googlemaps.Client(key='AIzaSyAzcr-SIFNGkVGbOJqhiaDoVw9OIV0NToQ')
now = datetime.now()


def gmaps(location=None):
    if location:
        if location == "work":
            directions_result = gmaps_request.directions("12235 Vance Jackson Rd, San Antonio, Texas",
                                                         "4440 S Piedras Dr #300, San Antonio, TX 78228",
                                                         mode="driving",
                                                         departure_time=now)
            route_time = (directions_result[0][u'legs'][0][u'duration_in_traffic'][u'text'])
            return route_time
        elif location == "school":
            directions_result = gmaps_request.directions("12235 Vance Jackson Rd, San Antonio, Texas",
                                                         "1 UTSA Circle, San Antonio, TX 78249",
                                                         mode="driving",
                                                         departure_time=now)
            route_time = (directions_result[0][u'legs'][0][u'duration_in_traffic'][u'text'])
            return route_time
    else:
        return None
