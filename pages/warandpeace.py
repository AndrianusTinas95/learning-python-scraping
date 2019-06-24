from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")

bsObj=BeautifulSoup(html , 'html.parser')
nameList = bsObj.findAll("span",{"class":"green"})

for name in nameList :
    print(name.get_text())