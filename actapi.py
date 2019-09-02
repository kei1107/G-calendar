# coding: UTF-8
from __future__ import print_function
import httplib2
from apiclient import discovery
from oauth2client import tools
import src
import sys
import time

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# setting logger
logger = src.Setup_Logger.Setup_Logger()

developer_flag = False


def main():
    mdid = None
    pw = None
    calendarid = None
    club_name = None
    activity_location = None
    table_path = None

    logger.info('Create Calendar events')
    time.sleep(0.1)
    if developer_flag is True:
        com = input('最新のテーブルデータを用いますか?(Do you use today\'s table data?) : (y/n) ')
        if com == 'n':
            # get Nu info
            mdid, pw, calendarid, club_name, activity_location = src.Setup_Config.Setup_Config(logger=logger)
            src.AccessGymReservationSystem.access(mdid=mdid, pw=pw, activity_location=activity_location, logger=logger)
        elif com == 'y':
            table_path = input('テーブルデータのパスを入力して下さい.(Please input table data path.) : ')
            calendarid, club_name, activity_location = src.Setup_Config.Setup_Config_non_idpw(logger=logger)
        else:
            logger.info('Your input command \"' + com + '\" is not defined.')
            logger.info('Program quit.')
            sys.exit()
    else:
        # get Nu info
        mdid, pw, calendarid, club_name, activity_location = src.Setup_Config.Setup_Config(logger=logger)
        src.AccessGymReservationSystem.access(mdid=mdid, pw=pw, activity_location=activity_location, logger=logger)

    time.sleep(0.1)
    bodys = src.CreateApi.create_api(club_name=club_name, activity_location=activity_location, logger=logger,
                                     table_path=table_path)
    print('======= Activity information =======', flush=True)
    for body in bodys:
        output_str = 'summary : ' + body['summary'] + ', start : ' + body['start']['dateTime'] + ', end : ' + \
                     body['end']['dateTime']
        print(output_str.replace('\xe9', ''), flush=True)
    print('====================================', flush=True)
    com = input('この情報をあなたのカレンダーに追加しますか？(Do you add this information to your calendar?) : (y/n) ')

    if com != 'y':
        if com != 'n':
            logger.info('Your input command \"' + com + '\" is not defined.')
        logger.info('Program quit.')
        sys.exit()

    credentials = src.Get_Credentials.get_credentials(flags=flags, logger=logger)
    try:
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)
        for body in bodys:
            event = service.events().insert(calendarId=calendarid, body=body).execute()
            logger.info('Event created: %s' % (event.get('htmlLink')))
    except Exception as e:
        logger.info('Error occured!')
        logger.exception(e)
        sys.exit()


if __name__ == '__main__':
    main()
