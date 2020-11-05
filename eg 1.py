import csv
with open('cars.csv') as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    for row in readcsv:
        print(row)

