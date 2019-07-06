from Core.Main import Scraping

html   = Scraping("http://en.wikipedia.org/wiki/Kevin_Bacon")
htmlOb = html.scriptData()

# for link in htmlOb.findAll("a") :
#     print(link.attr['href'])