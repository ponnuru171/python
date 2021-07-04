import csv
with open('test1.csv')as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    next(readcsv)
    for i in readcsv:
        print(i)