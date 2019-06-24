from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

class Sraping :

    @property
    def scriptData(self):
        pass
    
    @scriptData.setter
    def scriptData(self,url) :
        try:
            script = urlopen(url)
            self.__data = BeautifulSoup(script.read(),"html.parser")
            
        except HTTPError:
            self.__data = None
    
    @scriptData.getter
    def scriptData(self):
        return self.__data


html = Sraping()

html.scriptData = "https://www.tokopedia.com/kolling/garskin-laptop-art-hitam-orange-skin-laptop-stiker-laptop?src=topads"

data    = html.scriptData
search  = data.findAll(text="Terkirim")
print(len(search))
