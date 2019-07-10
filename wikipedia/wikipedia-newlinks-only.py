import os,sys,re

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from Core.Main import Scraping

pages = set()
url ="http://en.wikipedia.org"
def getLinks(pageUrl):
    global pages
    html = Scraping(url+pageUrl)
    htmlOb = html.scriptData()

    for link in htmlOb.findAll("a", href=re.compile("^(/wiki/)")):

        if 'href' in link.attrs :
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")