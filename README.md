# G-calendar

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

**Caution**  
Step3:quickstart.py

次のように書き換えて下さい  

Please rewritten as follows
```
L.20
SCOPES = 'https://www.googleapis.com/auth/calendar'
```


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
$ git clone https://github.com/kei1107/G-calendar
[download]
click 'Clone or download' -> 'Download ZIP'
```
### 3-2. add client_secret.json to G-calendar/json folder
client_secret.jsonファイル(2. Setting Prerequisites-Google Account and apiで使用したもの)を G-calendar/jsonフォルダに加えて下さい。

Plese add client_secret.json(used in 2.Setting Prerequisites-Google Account and api) to G-calendar/json folder
### 3-3. Setting config
G-calendar/config/settings.iniの情報を修正して下さい   

Please modify information in G-calendar/config/settings.ini

## 4. Execute
```
$ python actapi.py
```
