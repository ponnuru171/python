import csv
with open('cars.csv')as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    next(readcsv)
    for row in readcsv:
        print(row)