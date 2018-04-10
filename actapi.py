# coding: UTF-8
from __future__ import print_function
import httplib2
from apiclient import discovery

from pprint import pprint
import datetime
import src

# get Nu info
Mdid, Pw, CalendarId = src.Setup_Config.Setup_Config()


# CalendarId = 'l5flhg7ejf0svdv2sc0hun4bis@group.calendar.google.com'
# CalendarId = 'clavis1107@gmail.com'


def main():

    # src.AccessGymReservationSystem.access(Mdid, Pw)
    bodys = src.CreateApi.create_api(CalendarId)

    # setting logger
    logger = src.Setup_Logger.Setup_Logger()
    logger.info('Create Calendar events')

    credentials = src.Get_Credentials.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    print(CalendarId)
    for body in bodys:
        event = service.events().insert(calendarId=CalendarId, body=body).execute()
        print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':
    main()
