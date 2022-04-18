import requests, bs4
import time
from query import insert_data


URL_BASE = 'https://boardgamegeek.com/browse/boardgame/page/1'
bg_names = []
bg_links = []


def fetch_url(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.content, 'html.parser')
            return soup
    except requests.ReadTimeout:
        response = None


def get_boardgame_info(content):
    cont = 1
    for name in content.find_all('tr', id="row_"):
        bg_names.append(
            (name.find('div',  id = f'results_objectname{cont}').text.replace('\n', '')[:-6],
            name.find('div',  id = f'results_objectname{cont}').text.replace('\n', '')[-5:-1],
            name.find_all('td',  class_ = 'collection_bggrating')[-1].text.split().pop())
        )
        details = name.find('a',  class_ = 'primary')['href']
        page = f'https://boardgamegeek.com{details}'
        bg_links.append(page)
        insert_data(bg_names[len(bg_names)-1][0], bg_names[len(bg_names)-1][1], bg_names[len(bg_names)-1][2])
        cont += 1
    return bg_names
        

def next_page():
    for page in range(1,11):
        url = f'https://boardgamegeek.com/browse/boardgame/page/{page}'
        content = fetch_url(url)
        get_boardgame_info(content)
    return bg_names
