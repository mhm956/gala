
from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
import dateutil.parser

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_event_time(events):
    event_list = []
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_time = dateutil.parser.parse(start)
        event_time_string = "On the " + str(start_time.strftime('%A')) + ", you have " + event['summary'] + " at " + \
                            str(start_time.strftime('%-I')) + ":" + str(start_time.strftime('%M'))
        event_list.append(event_time_string)

    return event_list


def gcal():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    tomorrow = datetime.datetime.utcnow() + datetime.timedelta(days=2)
    tomorrow_formatted = tomorrow.isoformat("T") + "Z"
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, timeMax=tomorrow_formatted, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    # print(json.dumps(eventsResult, indent=4))
    events = eventsResult.get('items', [])
    time_date_string_dict = get_event_time(events)
    return time_date_string_dict
