import csv 
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
htmlOB = BeautifulSoup(html.read(),'html.parser')

table = htmlOB.findAll("table",{"class":"wikitable"})[0]
rows  = table.findAll("tr")

csvFile =open('storing/editor.csv','wt',newline='')
writer = csv.writer(csvFile)

try:
    for row in rows :
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text().rstrip("\n\r"))
            print(cell.get_text().rstrip("\n\r"))
        # print(csvRow)
        writer.writerow(csvRow)
finally:
    csvFile.close()
