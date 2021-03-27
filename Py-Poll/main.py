#Import Modules
import os
import csv
import math
import statistics

#set up variables
#total number of votes in the election
total_votes = 0
#% of total votes
votes_percent = 0.0000
#list with all the candidates
candidates = []
#number of votes for each candidate, w/ position in list corresponding to candidate's position in candidates list
num_of_votes=[]
#% of total votes for each candidate
percent_of_votes = []
#candidate that won the election and their votes
winner = " "
winningvotes = 0

#open up file
election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip top row containing the headers
    csv_header = next(csvreader)

    for row in csvreader:
        #total vote counter
        total_votes += 1

        #conditional to see if candidate is already in list
        if row[2] not in candidates:
            #add candidate to end of list if not in list
            candidates.append(row[2])
            #extracting index number of candidate in list
            index = candidates.index(row[2])
            #adding first vote to  candidate's vote index in vote list
            num_of_votes.append(1) 
        
        else:
            #extracting index number of candidate in candidates list
            index = candidates.index(row[2])
            #adding counter to  candidate's vote index in vote list
            num_of_votes[index] += 1
    #print(candidates)
    #print(num_of_votes)

    #resetting index to start at start of list
    index = 0
    while index < len(num_of_votes):
        votes_percent = float(num_of_votes[index])/float(total_votes)*100
        votes_percent = round(votes_percent, 3)
        percent_of_votes.append(votes_percent)
        index += 1
    #print(percent_of_votes)
    
    #winner is the one with the most votes
    winningvotes = max(num_of_votes)
    #find the winner's index
    index = num_of_votes.index(winningvotes)
    winner = candidates[index]

#fuction to print more line if there's more candidates
#set up start point
i = 0
#list for lines of text
lines = []
while i < len(candidates):
    #variable for each line of text
    # :.3f to round that number to 3 decimal places
    line= f"{candidates[i]}: {percent_of_votes[i]:.3f}% ({num_of_votes[i]} votes)"
    lines.append(line)
    i += 1
#final line for list printing candidates and votes is the winner of election
finalline = f"Winner: {winner}"
#add finalline to the lines list to be final entry to list
lines.append(finalline)
#for line in lines:
    #print(lines)
    
#Print to terminal
title = "Election Results"
linebreak = "---------------------------------------"
line2 = f"Total Votes: {total_votes}"
line4 = lines[0]
line5 = lines[1]
line6 = lines[2]
line7 = lines[3]
line8 = lines[4]
print(title)
print(linebreak)
print(line2)
print(linebreak)
#set up counter
i=0
#while loop set to stop before final line in list
while i < len(lines) - 1:
    print(lines[i])
    i += 1
if i == len(lines) - 1:
    #if statement is to add linebreak before announcing winner
    print(linebreak)
    print(lines[i])

#Create and write to new text file
output_file = open('Analysis/Election_Results.txt', 'w')
output_file.write(title + "\n")
output_file.write(linebreak + "\n")
output_file.write(line2 + "\n")
output_file.write(linebreak + "\n")
#set up counter
i=0
#while loop set to stop before final line in list
while i < len(lines) - 1:
    output_file.write(lines[i] + "\n")
    i += 1
#else when i = len(lines) - 1 meaning you're at last item on list
if i == len(lines)-1:
    #if statement is to add linebreak before announcing winner
    output_file.write(linebreak + "\n")
    output_file.write(lines[i] + "\n")
output_file.close()
