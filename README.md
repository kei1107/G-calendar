# NagoyaUniv_ActivityCalendar

[名古屋大学運動施設予約システム](http://133.6.82.138/undou/mudy0010c.php)から活動日を取得しGoogle Calendarに追加するプログラム  

Get activity dates from [Nagoya Univ. sports facility reservation system](http://133.6.82.138/undou/mudy0010c.php) and add it to Google Calendar.

Support : Windows , OSX

## 1. Prerequisites

Google  Account and api
---
Google Calendar及びapiが利用可能である  
Google Calendar and api enabled

Python
---
Python2   
**Python3**(Recommendation)

- pip package management tool
  - BeautifulSoup
  - pytz
  - selenium
  - google-api-python-client

Google Chrome
---
[Google Chrome](https://www.google.co.jp/chrome/index.html)  
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## 2. Setting Prerequisites
Google Account and api
---
日本語 ->  [Developers.IO](https://dev.classmethod.jp/cloud/google-calendar-api-get-start/)  
English -> [G Suite](https://developers.google.com/calendar/quickstart/python)

Python
---
```
$ pip install --upgrade beautifulsoup4
$ pip install --upgrade pytz
$ pip install --upgrade selenium
$ pip install --upgrade google-api-python-client
```

Google Chrome
---
Google Chrome及びChromeDriverのインストール  

Install Google Chrome and ChromeDriver  
[Google Chrome](https://www.google.co.jp/chrome/index.html)  
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)  

**環境変数PATHの設定を必ず行って下さい**

**It is essential to set PATH environment variable.**

## 3. Install
### 3-1. Clone or Download this repository
```
[clone]
$ https://github.com/kei1107/NagoyaUniv_ActivityCalendar
[download]
click 'Clone or download' -> 'Download ZIP'
```
### 3-2. add client_secret.json to "json folder"
client_secret.jsonファイル(2. Setting Prerequisites-Google Account and apiで使用したもの)を "jsonフォルダ"に加えて下さい。

Plese add client_secret.json(used in 2.Setting Prerequisites-Google Account and api) to "json folder"
### 3-3. Setting config
config/settings.iniの情報を修正して下さい
※保存形式 : **UTF-8**

Please modify information in config/settings.ini
※Save style : **UTF-8**

## 4. Execute
```
$ python actapi.py
```

## 5. Specification

プログラムを実行すると、[名古屋大学運動施設予約システム](http://133.6.82.138/undou/mudy0010c.php)にアクセスし、  
**当月分** の予定に関して活動日を取得、カレンダーへの書き込みを行います。  

When you run this program, this program access [Nagoya Univ. sports facility  
reservation system](http://133.6.82.138/undou/mudy0010c.php), and get activity schedules for this month.  
Then, the data is written to calendar.
