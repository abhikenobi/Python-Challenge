#Import Modules
import os
import csv

#set up variables
name= " "
first_name = []
last_name = []
dob = " "
new_dob = []
ssn = " "
new_ssn = []
state = " "
state_abbrev = []
employee_id = []
#import state abbreviations from: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
#https://gist.github.com/rogerallen/1583593 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employee_csv = os.path.join("Resources", "employee_data.csv")

with open(employee_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        #extract employee id #'s
        employee_id.append(row[0])
        #split name in each row using space as a delimiter
        name = row[1].split(" ")
        #add first split to first name list, second part to the last name list
        first_name.append(name[0])
        last_name.append(name[1])
        #split old dob with delimiter of -
        dob = row[2].split("-")
        new_dob.append(f"{dob[1]}/{dob[2]}/{dob[0]}")
        #split ssn using - as delimiter, add only the last split part to new list
        ssn = row[3].split("-")
        new_ssn.append(f"***-**-{ssn[2]}")
        #extract state name
        state = row[4]
        state_abbrev.append(f"{us_state_abbrev[state]}")
    #print(employee_id)
    #print(first_name)
    #print(last_name)
    #print(new_dob)
    #print(new_ssn)
    #print(state_abbrev)

    # Specify the file to write to
    output_path = os.path.join("Analysis", "cleaned_employee_data.csv")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

        # Use for loop to write rest of the rows
        index=0
        while index < len(employee_id):
            csvwriter.writerow([employee_id[index], first_name[index], last_name[index], new_dob[index], new_ssn[index], state_abbrev[index]])
            index += 1
