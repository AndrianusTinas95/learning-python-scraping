from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import random
import re,os,sys

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    htmlOB = BeautifulSoup(html.read(),'html.parser')
    return htmlOB.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl ="http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is: " + historyUrl)

    html = urlopen(historyUrl)
    htmlOB = BeautifulSoup(html.read(),'html.parser')

    ipAddresses = htmlOB.findAll("a",{"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks("/wiki/Kevin_Bacon")

while(len(links) > 0) :
    for link in links:
        print("-------------")
        historyIPs = getHistoryIPs(link.attrs["href"])

        for historyIP in historyIPs:
            print(historyIP)
    
    newLink = links[random.randint(0,len(links)-1)].attrs["href"]
    links = getLinks(newLink)