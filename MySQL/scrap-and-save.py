from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='mysql',charset='utf8')

cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

def store(title,content):
    cur.execute("INSERT INTO pages (title,content) VALUES(\"%s\",\"%s\")",(title,content))
    cur.connection.commit()

def getLinks(articleUrl):
    html    = urlopen("http://en.wikipedia.org"+articleUrl)
    htmlOB  = BeautifulSoup(html.read(),'html.parser')
    title   = htmlOB.find("h1").get_text()
    content = htmlOB.find("div",{"id":"mw-content-text"}).find("p").get_text()
    store(title.rstrip("\n\r"),content.rstrip("\n\r"))
    # print([title.rstrip("\n\r"),content.rstrip("\n\r")])
    return htmlOB.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

try:
    while len(links) > 0 :
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()