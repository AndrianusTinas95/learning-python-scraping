import os 
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://"+url
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url :
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl,"")
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    path = path.split("?",1)[0]

    return path

html = urlopen("http://www.pythonscraping.com")
htmlOB = BeautifulSoup(html.read(),"html.parser")
downloadList = htmlOB.findAll(src=True)

for download in downloadList :
    fileUrl = getAbsoluteURL(baseUrl,download["src"])
    if fileUrl is not None:
        print(fileUrl)
        file = getDownloadPath(baseUrl,fileUrl, downloadDirectory)
        urlretrieve(fileUrl,file)