import csv
with open('test1.csv')as csvfile:
    line=csvfile.readlines()
    print(len(line))
    readcsv=csv.reader(csvfile,delimiter=',')
    for row in readcsv:
        print(row)
