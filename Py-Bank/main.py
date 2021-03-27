#Import Modules
import os
import csv
import math
import statistics

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
netchange = []
#list for all the months/dates in the dataset
months= []

#set up file path
budget_csv = os.path.join("Resources", "budget_data.csv")

#read the csv file
with open(budget_csv) as csvfile:
    #use csvreader to read csv file
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #reading the header row to skip during iterations
    csv_header = next(csvreader)

    #have to extract first row of data to keep net monthly change in line with the rest of the data
    #sets loop's start point at 2nd row
    first_row = next(csvreader)
    
    #add the same counters as in the for loop
    totalmonths += 1
    net_total += int(first_row[1])
    
    #define previous month's profit/loss to get ready for the loop
    prev_profitloss = int(first_row[1])
    
    #set up equation to calculate change between current and previous month's profit/loss
    net_change = int(first_row[1]) - prev_profitloss

    for row in csvreader:
        #testing to see if loop works, comment out when code is finalized
        #print(row)

        #total months counter
        totalmonths += 1
        
        #net total counter (net total = prev. net total + this month's profit/loss)
        net_total += int(row[1])
        
        #add current month to months list
        months.append(row[0])
        
        #finding monthly change
        net_change = int(row[1]) - prev_profitloss
        
        #adding each months profit/loss to a list
        netchange.append(net_change)
        
        #set current month's profit/loss as previous for next loop
        prev_profitloss = int(row[1])

#calculate average monthly change, format to only show 2 decimal places
avg_monthly_change = round(statistics.mean(netchange), 2)

#print(avg_monthly_change)

#greatest incease, round in case of cents
maxincrease = round(max(netchange), 2)
max_month = months[netchange.index(maxincrease)]

#print(maxincrease)
#print(months[netchange.index(maxincrease)])

#greatest decrease, round in case of cents
minincrease = round(min(netchange), 2)
min_month = months[netchange.index(minincrease)]

#print(minincrease)
#print(months[netchange.index(minincrease)])

#print to terminal
print("--------------------------Financial Analysis------------------------")
print("--------------------------------------------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Net Total : ${net_total}")
print(f"Average Change: ${avg_monthly_change}")
print(f"Greatest Increase in Profits: {max_month}  (${maxincrease})")
print(f"Greatest Decrease in Profits: {min_month} (${minincrease})")

#Set up variables for each line of text
title = "--------------------------Financial Analysis------------------------"
line1 = "--------------------------------------------------------------------"
line2 = f"Total Months: {totalmonths}"
line3 = f"Net Total : ${net_total}"
line4 = f"Average Change: ${avg_monthly_change}"
line5 = f"Greatest Increase in Profits: {max_month}  (${maxincrease})"
line6 = f"Greatest Decrease in Profits: {min_month} (${minincrease})"
#write into .txt file in Analysis folder
output_file = open('Analysis/Financial_Analysis.txt', 'w')
output_file.write(title + "\n")
output_file.write(line1 + "\n")
output_file.write(line2 + "\n")
output_file.write(line3 + "\n")
output_file.write(line4 + "\n")
output_file.write(line5 + "\n")
output_file.write(line6 + "\n")
output_file.close()
