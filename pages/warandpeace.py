from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")

bsObj=BeautifulSoup(html , 'html.parser')

'''
nameList = bsObj.findAll("span",{"class":{"green","red"}})

for name in nameList :
    print(name.get_text())

print(len(nameList))

nameList = bsObj.findAll(text="the prince")
print(len(nameList))

nameList = bsObj.findAll({'h1','h2','h3','h4','h5','h6'})
for name in nameList :
    print(name.get_text())

nameList = bsObj.findAll(id="title")
for name in nameList :
    print(name.get_text())
'''