import csv
with open('csv_folder/test1.csv')as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')
    next(readcsv)
    for i in readcsv:
        print(i)