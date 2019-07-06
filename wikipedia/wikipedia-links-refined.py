import os,sys,re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Core.Main import Scraping

html   = Scraping("http://en.wikipedia.org/wiki/Kevin_Bacon")
htmlOb = html.scriptData()

for link in htmlOb.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")) :
    if 'href' in link.attrs :
        print(link.attrs['href'])
