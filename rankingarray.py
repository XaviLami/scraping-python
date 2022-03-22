import requests
from bs4 import BeautifulSoup
import requests_cache

requests_cache.install_cache('demo_cache')


class RankingScrapper(object):

    def __init__(self, url):
        self. url = url
        self.data = {}

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_infos(self):
        infos = []
        table = self.get_soup().find_all(class_="table")
        for content in table:
            infos.append(content.find('tr').get_text().replace("\n","").split())
            infos =infos[0][0] +' '+ infos[0][1]+' '+ infos[0][2] +' '+ infos[0][3] +' '+ infos[0][4] +' '+ infos[0][5]+infos[0][6]+' '+infos[0][7]+infos[0][8]+' '+infos[0][9]+' '+infos[0][10]+infos[0][11]+' '+infos[0][12]+infos[0][13]+infos[0][14]+' '+infos[0][15]+infos[0][16]+infos[0][17]
            return infos
    def get_datas(self):
        teams=[]
        table = self.get_soup().find_all(class_="team")
        # Si str concatener les éléments str
        for teamdatas in table:
           name = teamdatas.get_text().split()[0]+' '+teamdatas.get_text().split()[1]
           year = teamdatas.get_text().split()[2]
           wins = teamdatas.get_text().split()[3]
           losses = teamdatas.get_text().split()[4]
           print('Taille: ', len(teamdatas.get_text().split()))
           teams.append(name +' '+ year+' '+ wins+ ' '+ losses )
           print(teamdatas.get_text().split())
        print(teams)




if __name__ == "__main__":

    solution = RankingScrapper(r'http://www.scrapethissite.com/pages/forms/').get_infos()
    RankingScrapper(r'http://www.scrapethissite.com/pages/forms/').get_datas()

    print(solution)