import requests, bs4
import time
from query import insert_data


URL_BASE = 'https://boardgamegeek.com/browse/boardgame/page/1'
bg_names = []


def fetch_url(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.content, 'html.parser')
            return soup
    except requests.ReadTimeout:
        response = None


def get_boardgame_names(content):
    CONT = 1
    for name in content.find_all('tr', id="row_"):
        bg_names.append(
            (name.find('div',  id = f'results_objectname{CONT}').text.replace('\n', '')[:-6],
            name.find('div',  id = f'results_objectname{CONT}').text.replace('\n', '')[-5:-1]),
        )
        insert_data(bg_names[CONT-1][0], bg_names[CONT-1][1])
        CONT += 1
    return bg_names
        

def next_page():
    for page in range(1,11):
        url = f'https://boardgamegeek.com/browse/boardgame/page/{page}'
        content = fetch_url(url)
        # if content not in bg_names:
        get_boardgame_names(content)
    # return bg_names
    

# print(fetch_url(URL_BASE).find('div',  id = 'results_objectname1').text.split()[0])
# print(fetch_url(URL_BASE).find('tr div td td', id="row_").text.split()[0])
# print(get_boardgame_names(fetch_url(URL_BASE)))
print(next_page())
# print(len(next_page()))
print(bg_names)
# print(set(bg_names))

# a = [(1,2),(3,4),(5,6),(7,8),(9,0)]
# print(a[0][1])
# print(bg_names)