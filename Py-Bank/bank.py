#Import Modules
import os
import csv

#set up variables
total = 0
profitloss = []
changecalc = []
num_months = 0
datechange = []
totalchange = 0
avg_change = 0
maxincrease = 0
minincrease = 0
dateincrease = ''
datedecrease = ''

#set up file path
budget_csv = os.path.join("Resources", "budget_data.csv")

#read the csv file
with open(budget_csv) as csvfile:
    #use csvreader to read csv file
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #reading the header row
    csv_header = next(csvreader)
    #find total months
    #find the number of lines of data in the file
    #1 line = 1 month, so total month = length of file minus header
    totalmonths = len(list(csvreader))
    
    for row in csvreader:
        profitloss.append(int(row[1]))

        print(row)
    

#fint net total $

#average change

#greatest incease

#greatest decrease

#print to terminal
print("--------------------------Financial Analysis------------------------")
print("--------------------------------------------------------------------")
print(f"Total Months: {totalmonths}")
print(total)
#write into .txt file in Analysis folder
