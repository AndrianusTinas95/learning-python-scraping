from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

class Sraping :
    def __init__(self,url):
        self.__url = url

    def tes(self):
        print('tes ok')

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


html = Sraping('http://pythonscraping.com/pages/page1.html')
print(html.scriptData)
# print(html.__dict__)