import csv
with open('test1.csv')as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    next(readcsv)
    for row in readcsv:
        print(row)