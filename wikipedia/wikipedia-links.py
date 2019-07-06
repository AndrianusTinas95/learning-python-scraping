import os,sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Core.Main import Scraping

html   = Scraping("http://en.wikipedia.org/wiki/Kevin_Bacon")
htmlOb = html.scriptData()

for link in htmlOb.findAll("a") :
    if 'href' in link.attrs :
        print(link.attrs['href'])
