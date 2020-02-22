# -*- coding: utf-8 -*-
import os
import csv
import pandas as pd

#read in budget data

filepath = os.path.join("employee_data.csv")

Emp_ID = []
Name = []
DOB = []
SSN = []
State = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(reader)
    print("CSV Header: " + str(csv_header))
    
    for row in reader:
        Emp_ID.append(row[0])
        Name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        State.append(row[4])

First_Name = [x.split()[0] for x in Name] 
Last_Name = [x.split()[1] for x in Name] 
New_DOB = ['{}/{}/{}'.format(m,d,y) for y, m, d in map(lambda x: str(x).split('-'), DOB)]
New_SSN = [('***-**-' + x[-4:]) for x in SSN]


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
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
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

New_State = []

for x in State:
    x = us_state_abbrev.get(x,"")
    New_State.append(x)
    
df = pd.DataFrame(
    {'Emp ID': Emp_ID,
     'First Name': First_Name,
     'Last Name': Last_Name,
     'DOB': New_DOB,
     'SSN': New_SSN,
     'State': New_State 
    })
    
df.head()  

df.to_csv("employee_records.csv", index = None, header = True)