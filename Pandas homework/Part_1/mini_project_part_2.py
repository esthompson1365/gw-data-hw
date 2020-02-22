# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# Store filepath in a variable
file = "Resources/2016-FCC-New-Coders-Survey-Data.csv"

# Read our Data file with the pandas library
df = pd.read_csv(file, encoding="ISO-8859-1")

# search for specific column df.columns.get_loc("ExpectedEarning")

#index columns by number
df = df.iloc[:, [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 29, 30, 32, 36, 37, 45, 48, 56, 110, 111]]

#replace 0's with 'No' and 1's with 'Yes'
df['AttendedBootcamp'] = df['AttendedBootcamp'].replace(0,'No')
df['AttendedBootcamp'] = df['AttendedBootcamp'].replace(1,'Yes')

#subset df to get only people who attended bootcamp
df=df[df.AttendedBootcamp == 'Yes']

#Create a DataFrame with bootcamp name and the number of respondents who went to each bootcamp.
group_df = df.groupby("BootcampName")
#count rows for each bootcamp name
attendees = group_df.size()
#reset index
attendees = attendees.reset_index()

attendees=attendees.rename(columns = {0:'Attendees'})

#Create another DataFrame with bootcamp name and the number of respondents who recommend it.
recommenders = group_df['BootcampRecommend'].sum()
recommenders = recommenders.reset_index()

recommenders=recommenders.rename(columns = {'BootcampRecommend':'Recommendations'})

#Merge dataframes
merge_table = pd.merge(attendees, recommenders, on="BootcampName")
merge_table.head()

#Create a new column containing the percentage of respondents for each bootcamp who would recommend that bootcamp.
merge_table['Percent_Recommend'] = round(((merge_table['Recommendations']/merge_table['Attendees'])*100),2)

#Sort the new DataFrame in descending order of the percentage of recommenders you just calculated.
merge_table = merge_table.sort_values(by=['Percent_Recommend'], ascending=False)

#Use map and format to make the "% Recommended" column look more presentable.
merge_table['Percent_Recommend'] = merge_table['Percent_Recommend'].map("{:}%".format)

#Finally, export your DataFrame to an Excel file.
merge_table.to_csv("final_2.csv",header=True,index=False)f