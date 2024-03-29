from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError :
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        title = bsObj.body.h1
    except ArithmeticError as e:
        return None
    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")

if title == None :
    print("Title Could not be Found ")
else:
    print(title) 