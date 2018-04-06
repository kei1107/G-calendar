# coding: UTF-8
from __future__ import print_function
import httplib2
from apiclient import discovery

import datetime

import src

# get Nu info
Mdid, Pw, CalendarId = src.Setup_Config.Setup_Config()

# CalendarId = 'l5flhg7ejf0svdv2sc0hun4bis@group.calendar.google.com'
# CalendarId = 'clavis1107@gmail.com'


def main():
    src.CreateApi.CreateApi()

    return
    src.AccessGymReservationSystem.Access(Mdid, Pw)
    return

    # setting logger
    logger = src.Setup_Logger.Setup_Logger()
    logger.info('Create Calendar events')

    credentials = src.Get_Credentials.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId=CalendarId, timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == '__main__':
    main()
