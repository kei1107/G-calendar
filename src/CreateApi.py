from bs4 import BeautifulSoup
from pprint import pprint
i


def CreateApi():
    soup = BeautifulSoup(open('test.html', encoding='UTF-8'), 'html.parser')
    detail = soup.find(id='detail')
    trs = detail.find_all('tr')
    # pprint(trs[0])
    for td in trs[0].findAll('td'):
        pprint(td)
        pprint(td['colspan'])
        pprint(td.string)
        if td.span:
            pprint(td.span.string)
            if (td.span.string.find('Trébol')):
                print('ok')
        print('=========================================')

    # pprint(type(trs[0]))
