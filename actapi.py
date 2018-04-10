# coding: UTF-8
from __future__ import print_function
import httplib2
from apiclient import discovery
from oauth2client import tools
from pprint import pprint
import src
import sys

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# get Nu info
mdid, pw, calendarId, club_name, activity_location = src.Setup_Config.Setup_Config()
# setting logger
logger = src.Setup_Logger.Setup_Logger()


def main():
    logger.info('Create Calendar events')
    src.AccessGymReservationSystem.access(mdid=mdid, pw=pw, activity_location=activity_location, logger=logger)
    bodys = src.CreateApi.create_api(club_name=club_name, activity_location=activity_location, logger=logger)
    pprint(bodys)
    credentials = src.Get_Credentials.get_credentials(flags=flags, logger=logger)
    try:
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)
        for body in bodys:
            event = service.events().insert(calendarId=calendarId, body=body).execute()
            logger.info('Event created: %s' % (event.get('htmlLink')))
    except Exception as e:
        logger.info('Error occured!')
        logger.exception(e)
        sys.exit()


if __name__ == '__main__':
    main()
