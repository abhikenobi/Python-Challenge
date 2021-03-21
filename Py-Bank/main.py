#Modules needed for csv
import os
import csv

#Set a path for the csv file
csvpath = os.path.join("Resources","budget_data.csv")

#Use csvreader Module to read csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        print(row)

    



