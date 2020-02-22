# -*- coding: utf-8 -*-
import os
import csv

#read in budget data

filepath = os.path.join("budget_data.csv")

date = []
profit_losses = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    
    
    reader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(reader)
    print("CSV Header: " + str(csv_header))
    
    for row in reader:
        date.append(row[0])
        profit_losses.append(int(row[1]))
        total_months = len(date)
        total = sum(profit_losses)
        
# Calculating difference list 
diff_profit = [] 
for x, y in zip(profit_losses[0::], profit_losses[1::]): 
    diff_profit.append(y-x) 
    
def Average(lst): 
    return sum(lst) / len(lst) 

avg_diff = round(Average(diff_profit),2)
min_diff = min(diff_profit)
max_diff = max(diff_profit)
index_min =  (diff_profit.index(min(diff_profit))+1)     
date_min = date[index_min]
index_max =  (diff_profit.index(max(diff_profit))+1)     
date_max = date[index_max]

#string together and print result

str1 = "Financial Analysis"
str2 = "----------------------------"
str3 = ("Total Months: " + str(total_months))
str4 = ("Total: $" + str(total))
str5 = ("Average Change: $" + str(avg_diff))
str6 = ("Greatest Increse in Profits: (" + str(date_max) +") " + str(max_diff))
str7 = ("Greatest Decrease in Profits: (" + str(date_min) +") " + str(min_diff))

a = '\n'.join([str1,str2,str3,str4,str5,str6,str7])
print(a)

#save results to txt
file = open('results.txt','w') 
 
file.write(a) 

file.close() 