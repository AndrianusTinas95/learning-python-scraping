import os,sys,re,datetime,random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Core.Main import Scraping

random.seed(datetime.datetime.now())

def getLinks(articleUrl) :

    html   = Scraping("http://en.wikipedia.org" + articleUrl)
    htmlOb = html.scriptData()
    return htmlOb.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0 :
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)