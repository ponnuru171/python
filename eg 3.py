import csv
with open('products.csv') as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    for row in readcsv:
        print(row[0])
