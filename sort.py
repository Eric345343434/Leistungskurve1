import csv

with open("activity.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei, delimiter=";")
    for row in csv_reader_object:
        print(row)