#Modules needed for csv
import os
import csv

#Set a path for the csv file
csvpath = os.path.join("Resources","budget_data.csv")

#Use csvreader Module to read csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print("Financial Analysis")
    print("---------------------------------")
    
    #creating a list for each month in the csv file
    month = []

    #list for proftloss
    profitloss = []

    #initial value and variable for net total
    total = 0

    for row in csvreader:
        
        # adding each month to the month list
        month.append(row[0])

        #adding each month's proft/loss to list
        profitloss.append(row[1])
    
    profitloss.pop(0)
    
    for x in profitloss:
        #add profit/losses from each month to the net total
        total = sum(profitloss)
    
    #finding the total number of months by finding the lenght -1 because of the header
    #could also do mylist.pop(0) to remove header from list and print out len(month) instead
    print(f"Total Month : {len(month)-1}")

    print(f" Net Total : {net_total}")








