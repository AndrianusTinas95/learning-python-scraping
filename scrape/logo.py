from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html    = urlopen('http://www.pythonscraping.com')
htmlOB  = BeautifulSoup(html.read(),'html.parser')
imageLocation=htmlOB.find("a",{"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation,'logo.jpg')