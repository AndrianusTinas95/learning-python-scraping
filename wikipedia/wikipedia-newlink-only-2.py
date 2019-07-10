import os,sys,re

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from Core.Main import Scraping

pages = set()
url ="http://en.wikipedia.org"
def getLinks(pageUrl):
    global pages
    html = Scraping(url+pageUrl)
    htmlOb = html.scriptData()
    
    try:
        print("H1: ", htmlOb.h1.get_text())
        print("1st paragraph: \n", htmlOb.find(id = "mw-content-text").findAll('p')[0])
        print("edit link: ", htmlOb.find(id = "ca-edit").find("span").find("a").attrs['href'])

    except AttributeError:
        print(" this page is missing something ! no worries though !")

    for link in htmlOb.findAll("a", href=re.compile("^(/wiki/)")):

        if 'href' in link.attrs :
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("-----------------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")