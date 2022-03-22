import requests
from bs4 import BeautifulSoup
import requests_cache

requests_cache.install_cache('demo_cache')


class DevicesScrapper(object):
    def __init__(self, url):
        self.url = url
        self.data = {}

    def get_request(self):
        return requests.get(self.url).text
    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')


    def get_devices(self):
        rows = self.get_soup().find("div", {"class": "row"})
        for row in rows:
            columns = row.find_all("div", {"col-sm-4 col-lg-4 col-md-4"}, limit=3)
            save = []
            for cell in columns[1:]:
                title_info = list(map(lambda data: data.get_text().strip(), cell))
                save.append(list(filter(lambda data: data, title_info)))
            self.data[f'{" ".join(save[0])}'] = save[1][0]

        return self.data
if __name__ == "__main__":

    computer_page = DevicesScrapper(r'https://webscraper.io/test-sites/e-commerce/allinone/computers').get_devices()
    print(computer_page)
