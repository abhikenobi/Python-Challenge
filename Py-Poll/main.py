#Import Modules
import os
import csv
import math
import statistics

#set up variables
#total number of votes in the election
total_votes = 0
#list with all the candidates
candidates = []
#number of votes for each candidate, w/ position in list corresponding to candidate's position in candidates list
num_of_votes=[]
#% of total votes for each candidate
vote_percent = []

#open up file
election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

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
while candidates:
    

#Goals
#Total # of votes cast -done
#Complete list of candidates who received votes -done
#Percentage of total votes each candidate won
#Total number of votes each candidate won
#Winner based on popular election

#Print to terminal
print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------")
#Create and write to new text file