import os
import configparser


def Setup_Config():
    config_dif_path = os.path.join(os.path.abspath('.'), 'config')
    config_file_path = os.path.join(config_dif_path, 'settings.ini')
    config_file = configparser.SafeConfigParser()
    config_file.read(config_file_path)

    return config_file.get('settings', 'Mdid', ), \
           config_file.get('settings', 'Pw'),
