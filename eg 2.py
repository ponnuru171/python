import csv
with open('human.csv') as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    next(readcsv)
    for row in readcsv:
        print(row)
