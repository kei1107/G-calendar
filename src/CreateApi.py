from bs4 import BeautifulSoup
from pprint import pprint
import datetime
import pytz

'''
datetime -> RFC3339

<https://qiita.com/estaro/items/2b7074839d2a5e883dc1>

def iso_to_jstdt(iso_str)
'''


def create_api(calendar_id):
    '''
    base_time = datetime.datetime.now()
    start_time = base_time + datetime.timedelta(days=1)
    end_time = base_time + datetime.timedelta(days=1, hours=1)

    start_time = start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat()
    end_time = end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat()

    body = {
        "summary": "",
        "start": {
            "dateTime": start_time,
            "timeZone": "Asia/Tokyo",
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "Asia/Tokyo",
        }
    }
    '''

    bodys = []
    base_time = datetime.datetime.now()
    base_time = base_time - datetime.timedelta(hours=base_time.hour, minutes=base_time.minute, seconds=base_time.second,
                                               microseconds=base_time.microsecond) + datetime.timedelta(hours=7)
    #    print(base_time)

    soup = BeautifulSoup(open('scraping-data/test.html', encoding='UTF-8'), 'html.parser')
    detail = soup.find(id='detail')
    trs = detail.find_all('tr')

    for tr in trs[0::2]:
        have_circle = False
        start_time = base_time
        end_time = base_time
        now_time = base_time

        for td in tr.findAll('td'):
            try:
                active_min = int(td['colspan']) * 15
                if td.span and (td.span.string.find('Trébol') != -1):
                    if have_circle is False:
                        start_time = now_time
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                        have_circle = True
                    else:
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                else:
                    now_time = now_time + datetime.timedelta(minutes=active_min)

            except Exception as e:
                print(e)

        if have_circle is True:
            bodys.append({
                "summary": "Trébol 練習日",
                "start": {
                    "dateTime": start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                    "timeZone": "Asia/Tokyo",
                },
                "end": {
                    "dateTime": end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                    "timeZone": "Asia/Tokyo",
                }
            })
        base_time = base_time + datetime.timedelta(days=1)

    return bodys
