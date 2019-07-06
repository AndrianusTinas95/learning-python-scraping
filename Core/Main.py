from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

class Scraping :

    def __init__(self,url) :
        self.__url = url
        print('you are scraper ? ')

    @property
    def url(self) :
        pass
    
    @url.setter
    def url(self,url) :
        self.__url = url
    
    @url.getter
    def url(self):
        return self.__url

    def scriptData(self):
        try:
            script = urlopen(self.url)
            self.__data = BeautifulSoup(script.read(),"html.parser")
            
        except HTTPError:
            self.__data = None

        return self.__data


# html = Scraping("https://www.tokopedia.com/kolling/garskin-laptop-art-hitam-orange-skin-laptop-stiker-laptop?src=topads")


# data    = html.scriptData()
# search  = data.findAll("h1")
# print(search)
