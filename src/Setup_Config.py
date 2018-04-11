import os
import configparser
import sys


def Setup_Config(logger):
    config_dif_path = os.path.join(os.path.abspath('.'), 'config')
    config_file_path = os.path.join(config_dif_path, 'settings.ini')
    config_file = configparser.SafeConfigParser()
    config_file.read(config_file_path)

    mdid = config_file.get('settings', 'mdid')
    pw = config_file.get('settings', 'pw')
    calendarid = config_file.get('settings', 'calendarid')
    club_name = config_file.get('settings', 'club_name')
    activity_location = config_file.get('settings', 'activity_location')

    default_str = 'Default'
    if mdid == default_str or pw == default_str or calendarid == default_str or club_name == default_str or activity_location == default_str:
        logger.info('Found default setting in settings.ini. Please check and modify.')
        sys.exit()
    return mdid, pw, calendarid, club_name, activity_location


def Setup_Config_non_idpw(logger):
    config_dif_path = os.path.join(os.path.abspath('.'), 'config')
    config_file_path = os.path.join(config_dif_path, 'settings.ini')
    config_file = configparser.SafeConfigParser()
    config_file.read(config_file_path)

    calendarid = config_file.get('settings', 'calendarid')
    club_name = config_file.get('settings', 'club_name')
    activity_location = config_file.get('settings', 'activity_location')

    default_str = 'Default'
    if calendarid == default_str or club_name == default_str or activity_location == default_str:
        logger.info('Found default setting in settings.ini. Please check and modify.')
        sys.exit()
    return calendarid, club_name, activity_location
