import json
from requests import get
from bs4 import BeautifulSoup

stream_page_url = 'https://ondemand.parliament.nz/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
}

class Stream(object):
    __watch_page_html = BeautifulSoup(get(stream_page_url, headers=headers).text, 'lxml')

    @property
    def stream_url(self):
        return json.loads(self.__watch_page_html.find('script', {'type': 'text/javascript'}).string.strip()[34:-3])[0]['Uri']

    @property
    def is_live(self):
        if self.__watch_page_html.find('h2', {'class': 'hero-tile__title'}).text.strip() == 'The House is not currently sitting':
            return False
        else:
            return True
        
    @property
    def stream_urls(self):
        return({'lower': self.stream_url})