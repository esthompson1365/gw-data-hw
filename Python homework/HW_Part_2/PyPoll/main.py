# -*- coding: utf-8 -*-
import os
import csv

#read in budget data

filepath = os.path.join("election_data.csv")

voter_id = []
county = []
candidate = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    
    
    reader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(reader)
    print("CSV Header: " + str(csv_header))
    
    for row in reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

total_votes = len(voter_id)

#unique candidates
unique_candidates = []  
    
def unique(lst):      
    # traverse for all elements 
    for x in lst: 
        # check if exists in unique_list or not 
        if x not in unique_candidates: 
            unique_candidates.append(x)         
    for x in unique_candidates: 
        print(x)
        
unique(candidate)

Khan_votes = candidate.count("Khan")
Correy_votes = candidate.count("Correy")        
Li_votes = candidate.count("Li")
OTooley_votes = candidate.count("O'Tooley")

Khan_percent = "%.3f" %(Khan_votes/total_votes*100)
Correy_percent = "%.3f" %(Correy_votes/total_votes*100)
Li_percent = "%.3f" %(Li_votes/total_votes*100)
OTooley_percent = "%.3f" %(OTooley_votes/total_votes*100)

poll_dict = {
        "Khan": Khan_votes,
        "Correy": Correy_votes,
        "Li": Li_votes,
        "O'Tooley": OTooley_votes
        }

import operator

winner = max(poll_dict.items(), key=operator.itemgetter(1))[0]

#string together and print result

str1 = "Election Results"
line = "----------------------------"
str2 = ("Total Votes: " + str(total_votes))

str3 = ("Khan: " + str(Khan_percent) + "% (" + str(Khan_votes) + ")")
str4 = ("Correy: " + str(Correy_percent) + "% (" + str(Correy_votes) + ")")
str5 = ("Li: " + str(Li_percent) + "% (" + str(Li_votes) + ")")
str6 = ("O'Tooley: " + str(OTooley_percent) + "% (" + str(OTooley_votes) + ")")

str7 = ("Winner: " + str(winner))

a = '\n'.join([str1,line,str2,line,str3,str4,str5,str6,line,str7])
print(a)

#save results to txt
file = open('results.txt','w') 
 
file.write(a) 

file.close() 
