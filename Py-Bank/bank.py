#Import Modules
import os
import csv

#set up variables
#the total profit/loss for the whole dataset
net_total = 0
#previous month's profit/loss
prev_profitloss = 0
#the total number of months/rows in the dataset
totalmonths = 0
#average between the change in each month's profit/loss
avg_monthly_change = 0
#the greatest positive change in each month's profit/loss
maxincrease = 0
#the greatest negative change in each month's profit/loss
minincrease = 0
#the change in each month's profit/loss
net_change = 0
#list to house all the monthly changes in profit/loss
netchange =[]

#set up file path
budget_csv = os.path.join("Resources", "budget_data.csv")

#read the csv file
with open(budget_csv) as csvfile:
    #use csvreader to read csv file
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #reading the header row to skip during iterations
    csv_header = next(csvreader)

    #have to extract first row of data to keep net monthly change in line with the rest of the data
    first_row = next(csvreader)
    #add the same counters as in the for loop
    totalmonths += 1
    net_total += int(first_row[1])
    net_change = nettotal - int(first_row[1])
    #define previous month's profit/loss, to get ready for the loop
    prevtotal = int(first_row[1])

    for row in csvreader:
        #testing to see if loop works, comment out when code is finalized
        #print(row)
        #total months counter
        totalmonths += 1
        #net total counter (net total = prev. net total + this month's profit/loss)
        nettotal += int(row[1])

        #finding monthly change
        #adding each months profit/loss to a list
        netchange.append(int(row[1]))

#average change

#greatest incease

#greatest decrease

#print to terminal
print("--------------------------Financial Analysis------------------------")
print("--------------------------------------------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Net Total : ${nettotal}")
#write into .txt file in Analysis folder
