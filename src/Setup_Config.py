import os
import configparser


def Setup_Config():
    config_dif_path = os.path.join(os.path.abspath('.'), 'config')
    config_file_path = os.path.join(config_dif_path, 'settings.ini')
    config_file = configparser.SafeConfigParser()
    config_file.read(config_file_path)

    return config_file.get('settings', 'mdid', ), \
           config_file.get('settings', 'pw'), \
           config_file.get('settings', 'calendarId'), \
           config_file.get('settings', 'club_name'), \
           config_file.get('settings', 'activity_location'),
