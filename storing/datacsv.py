import csv

csvfile = open("storing/tes.csv","w+",newline='')
try:
    writer = csv.writer(csvfile)
    writer.writerow(('number','number plus 2','number timer 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvfile.close()
