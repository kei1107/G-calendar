from bs4 import BeautifulSoup
import datetime
import pytz
import sys


def location0(trs, base_time, club_name):
    bodys = []
    location = {0: '(陸上競技場/フィールド北側)', 1: '(陸上競技場/フィールド南側)'}
    for i in range(0, len(trs), len(location)):
        for j in range(len(location)):
            tr = trs[i + j]
            have_circle = False
            start_time = base_time
            end_time = base_time
            now_time = base_time
            for td in tr.findAll('td'):
                active_min = int(td['colspan']) * 15
                if td.text and (td.text.find(club_name) != -1):
                    if have_circle is False:
                        start_time = now_time
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                        have_circle = True
                    else:
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                else:
                    if have_circle is True:
                        bodys.append({
                            'summary': club_name + '活動日' + location[j],
                            'start': {
                                'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            },
                            'end': {
                                'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            }
                        })
                        have_circle = False
                    now_time = now_time + datetime.timedelta(minutes=active_min)

            if have_circle is True:
                bodys.append({
                    'summary': club_name + '活動日' + location[j],
                    'start': {
                        'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    },
                    'end': {
                        'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    }
                })
        base_time = base_time + datetime.timedelta(days=1)
    return bodys


def location1(trs, base_time, club_name):
    bodys = []
    location = {0: '(多目的コート/多目的コート)'}
    for i in range(0, len(trs), len(location)):
        for j in range(len(location)):
            tr = trs[i + j]
            have_circle = False
            start_time = base_time
            end_time = base_time
            now_time = base_time
            for td in tr.findAll('td'):
                active_min = int(td['colspan']) * 15
                if td.text and (td.text.find(club_name) != -1):
                    if have_circle is False:
                        start_time = now_time
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                        have_circle = True
                    else:
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                else:
                    if have_circle is True:
                        bodys.append({
                            'summary': club_name + '活動日' + location[j],
                            'start': {
                                'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            },
                            'end': {
                                'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            }
                        })
                        have_circle = False
                    now_time = now_time + datetime.timedelta(minutes=active_min)

            if have_circle is True:
                bodys.append({
                    'summary': club_name + '活動日' + location[j],
                    'start': {
                        'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    },
                    'end': {
                        'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    }
                })
        base_time = base_time + datetime.timedelta(days=1)
    return bodys


def location2(trs, base_time, club_name):
    bodys = []
    location = {0: '(野球場/野球場)'}
    for i in range(0, len(trs), len(location)):
        for j in range(len(location)):
            tr = trs[i + j]
            have_circle = False
            start_time = base_time
            end_time = base_time
            now_time = base_time
            for td in tr.findAll('td'):
                active_min = int(td['colspan']) * 15
                if td.text and (td.text.find(club_name) != -1):
                    if have_circle is False:
                        start_time = now_time
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                        have_circle = True
                    else:
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                else:
                    if have_circle is True:
                        bodys.append({
                            'summary': club_name + '活動日' + location[j],
                            'start': {
                                'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            },
                            'end': {
                                'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            }
                        })
                        have_circle = False
                    now_time = now_time + datetime.timedelta(minutes=active_min)

            if have_circle is True:
                bodys.append({
                    'summary': club_name + '活動日' + location[j],
                    'start': {
                        'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    },
                    'end': {
                        'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    }
                })
        base_time = base_time + datetime.timedelta(days=1)
    return bodys


def location3(trs, base_time, club_name):
    bodys = []
    location = {0: '(硬式テニスコート/1面)', 1: '(硬式テニスコート/2面)', 2: '(硬式テニスコート/3面)', 3: '(硬式テニスコート/4面)', 4: '(硬式テニスコート/5面)',
                5: '(硬式テニスコート/6面)', 6: '(硬式テニスコート/7面)'}
    for i in range(0, len(trs), len(location)):
        for j in range(len(location)):
            tr = trs[i + j]
            have_circle = False
            start_time = base_time
            end_time = base_time
            now_time = base_time
            for td in tr.findAll('td'):
                active_min = int(td['colspan']) * 15
                if td.text and (td.text.find(club_name) != -1):
                    if have_circle is False:
                        start_time = now_time
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                        have_circle = True
                    else:
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                else:
                    if have_circle is True:
                        bodys.append({
                            'summary': club_name + '活動日' + location[j],
                            'start': {
                                'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            },
                            'end': {
                                'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            }
                        })
                        have_circle = False
                    now_time = now_time + datetime.timedelta(minutes=active_min)

            if have_circle is True:
                bodys.append({
                    'summary': club_name + '活動日' + location[j],
                    'start': {
                        'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    },
                    'end': {
                        'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    }
                })
        base_time = base_time + datetime.timedelta(days=1)
    return bodys


def location4(trs, base_time, club_name):
    base_time = base_time + datetime.timedelta(hours=2)
    bodys = []
    location = {0: '(新体育館アリーナ/アリーナ)'}
    for i in range(0, len(trs), len(location)):
        for j in range(len(location)):
            tr = trs[i + j]
            have_circle = False
            start_time = base_time
            end_time = base_time
            now_time = base_time
            for td in tr.findAll('td'):
                active_min = int(td['colspan']) * 15
                if td.text and (td.text.find(club_name) != -1):
                    if have_circle is False:
                        start_time = now_time
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                        have_circle = True
                    else:
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                else:
                    if have_circle is True:
                        bodys.append({
                            'summary': club_name + '活動日' + location[j],
                            'start': {
                                'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            },
                            'end': {
                                'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            }
                        })
                        have_circle = False
                    now_time = now_time + datetime.timedelta(minutes=active_min)

            if have_circle is True:
                bodys.append({
                    'summary': club_name + '活動日' + location[j],
                    'start': {
                        'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    },
                    'end': {
                        'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    }
                })
        base_time = base_time + datetime.timedelta(days=1)
    return bodys


def location5(trs, base_time, club_name):
    bodys = []
    location = {0: '(第１体育館/入り口側)', 1: '(第１体育館/奥側)'}
    for i in range(0, len(trs), len(location)):
        for j in range(len(location)):
            tr = trs[i + j]
            have_circle = False
            start_time = base_time
            end_time = base_time
            now_time = base_time
            for td in tr.findAll('td'):
                active_min = int(td['colspan']) * 15
                if td.text and (td.text.find(club_name) != -1):
                    if have_circle is False:
                        start_time = now_time
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                        have_circle = True
                    else:
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                else:
                    if have_circle is True:
                        bodys.append({
                            'summary': club_name + '活動日' + location[j],
                            'start': {
                                'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            },
                            'end': {
                                'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            }
                        })
                        have_circle = False
                    now_time = now_time + datetime.timedelta(minutes=active_min)

            if have_circle is True:
                bodys.append({
                    'summary': club_name + '活動日' + location[j],
                    'start': {
                        'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    },
                    'end': {
                        'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    }
                })
        base_time = base_time + datetime.timedelta(days=1)
    return bodys


def location6(trs, base_time, club_name):
    bodys = []
    location = {0: '(第１体育館/入り口側)', 1: '(第１体育館/奥側)'}
    for i in range(0, len(trs), len(location)):
        for j in range(len(location)):
            tr = trs[i + j]
            have_circle = False
            start_time = base_time
            end_time = base_time
            now_time = base_time
            for td in tr.findAll('td'):
                active_min = int(td['colspan']) * 15
                if td.text and (td.text.find(club_name) != -1):
                    if have_circle is False:
                        start_time = now_time
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                        have_circle = True
                    else:
                        now_time = now_time + datetime.timedelta(minutes=active_min)
                        end_time = now_time
                else:
                    if have_circle is True:
                        bodys.append({
                            'summary': club_name + '活動日' + location[j],
                            'start': {
                                'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            },
                            'end': {
                                'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                                'timeZone': 'Asia/Tokyo',
                            }
                        })
                        have_circle = False
                    now_time = now_time + datetime.timedelta(minutes=active_min)

            if have_circle is True:
                bodys.append({
                    'summary': club_name + '活動日' + location[j],
                    'start': {
                        'dateTime': start_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    },
                    'end': {
                        'dateTime': end_time.astimezone(pytz.timezone('Asia/Tokyo')).isoformat(),
                        'timeZone': 'Asia/Tokyo',
                    }
                })
        base_time = base_time + datetime.timedelta(days=1)
    return bodys


def create_api(club_name, activity_location, logger, table_path=None):
    base_time = datetime.datetime.now()
    base_time = base_time - datetime.timedelta(hours=base_time.hour, minutes=base_time.minute, seconds=base_time.second,
                                               microseconds=base_time.microsecond) + datetime.timedelta(hours=7)
    soup = BeautifulSoup(
        open((lambda x: 'scraping-data/index' + activity_location + '.html' if x is None else x)(table_path),
             encoding='UTF-8'), 'html.parser')
    detail = soup.find(id='detail')
    if detail is None:
        logger.info('Cann\'t open index' + activity_location + '.html')
        sys.exit()
    trs = detail.find_all('tr')
    bodys = eval('location' + activity_location)(trs=trs, base_time=base_time, club_name=club_name)
    return bodys
