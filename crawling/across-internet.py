from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

import re,datetime,random


pages =set()
random.seed(datetime.datetime.now())

# Retrieves a list of all Internal Link found on a page
def getInternalLinks(bsObj,includeUrl):
    includeUrl  = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []

    #find all links that begin with a "/"
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+"+)")):
        if link.attrs['href'] is not None :
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    
    return internalLinks



# Retrieves a list of all external links found on a page 

def getExternalLinks(bsobj,excludeUrl):
    externalLinks=[]

    #finds all links that start "http" that to not contain the current URL
    for link in bsobj.findAll("a", href=re.compile("(^http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks :
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    # bsobj = BeautifulSoup(html,"lxml")
    bsobj = BeautifulSoup(html.read(),'html.parser')

    externalLinks = getExternalLinks(bsobj,urlparse(startingPage).netloc)
    if len(externalLinks) == 0 :
        print("No External Links, looking around the site for one")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsobj,domain)
        print(len(internalLinks))
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)] 


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random External link is",externalLink)
    followExternalOnly(externalLink)

#Collects a list of all external URLs found on the site
allExtLinks =set()
allIntLinks =set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
    bsobj = BeautifulSoup(html.read(),'html.parser')

    externalLinks   = getExternalLinks(bsobj,domain)
    internalLinks   = getInternalLinks(bsobj,domain)

    for link in externalLinks :
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)

    for link in internalLinks :
        if link not in allIntLinks:
            allIntLinks.add(link)
            print("----------------------new link --------------\n")
            getAllExternalLinks(link)

url = "https://www.python.org/"

allIntLinks.add("http:www.python.org")
getAllExternalLinks(url)
followExternalOnly(url)


# startingPage = "http://python.org"

# html = urlopen(startingPage)
# bsobj = BeautifulSoup(html.read(),'html.parser')

# domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
# internalLinks = getInternalLinks(bsobj,domain)
# for link in internalLinks :
#     print(link)