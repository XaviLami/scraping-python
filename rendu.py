import requests
from bs4 import BeautifulSoup
import requests_cache

requests_cache.install_cache('demo_cache')

class WikiScrapper(object):
    def __init__(self, url):
        self. url = url
        self.data = {}

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_title(self):
        title = self.get_soup().find('h1').get_text()
        return title
    def get_description(self):
        block = self.get_soup().find('div', {'class': 'mw-parser-output'})
        par_description = block.findChildren("p", recursive=False)
        for child in par_description:
            description = child.get_text()
        return description
    def get_summary(self):
        title = self.get_soup().find(class_="toctitle").get_text()

        div = self.get_soup().find(class_="toc")
        ul = div.findChildren("ul", recursive=False)
        for child in ul:
            list = child.get_text().strip()
        return title + "\n" + list
    def get_second_title(self):
        title = self.get_soup().find(class_="mw-headline").get_text()
        return "\n"+ title
    def get_color_array(self):
        table = self.get_soup().find(class_="wikitable champions-list-legend").tbody
        tr = table.find_all('tr')
        data = []
        for i in tr:
            table_data = i.find_all('td')
            result = [j.text.replace("\n", "") for j in table_data]
            data.append(result)
        return data

    def get_legend_array(self):
        save_head =[]
        save_body = []
        t_head = self.get_soup().find(class_='article-table')
        save_head.append(t_head.get_text().replace("\n"," ")[0:67])
        save_body.append(t_head.get_text().replace("\n"," ")[67:])
        return [save_head] + [save_body]

    def get_title_cost_reduction(self):
        title = self.get_soup().find("h3").get_text()
        return title
    def get_list_of_scraped_champions(self):
        title = self.get_soup().find("span", {"id": "List_of_Scrapped_Champions"}).get_text()
        div = self.get_soup().find(class_="columntemplate").get_text()
        return title + div

    def get_reference(self):
        title = self.get_soup().find("span", {"id": "References"}).get_text()
        title_array = self.get_soup().find(class_="mw-collapsible-header").get_text()
        table = self.get_soup().find(class_="navbox").get_text()
        return title + title_array + table

if __name__ == "__main__":

    title = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_title()
    description = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_description()
    summary = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_summary()
    second_title = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_second_title()
    color_array = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_color_array()
    table_legend = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_legend_array()
    three_title = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_title_cost_reduction()
    reference = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_reference()
    scraped_champions = WikiScrapper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_list_of_scraped_champions()
    print(title)
    print(description)
    print(summary)
    print(second_title)
    print(color_array)
    print(table_legend)
    print(three_title)
    print(scraped_champions)
    print(reference)