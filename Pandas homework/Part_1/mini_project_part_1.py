# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# Store filepath in a variable
file = "Resources/2016-FCC-New-Coders-Survey-Data.csv"

# Read our Data file with the pandas library
df = pd.read_csv(file, encoding="ISO-8859-1")
df.columns.get_loc("ExpectedEarning")

#index columns by number
df = df.iloc[:, [0, 1, 2, 3, 6, 7, 8, 9, 10, 28, 29, 31, 34, 35, 36, 44, 47, 55, 109, 110]]


#replace 0's with 'No' and 1's with 'Yes'
df['AttendedBootcamp'] = df['AttendedBootcamp'].replace(0,'No')
df['AttendedBootcamp'] = df['AttendedBootcamp'].replace(1,'Yes')

#total responses (number of rows)
total_respondents = len(df)

#subset df to get only people who attended bootcamp
df2=df[df.AttendedBootcamp == 'Yes']

#total attendees (number of rows)
total_attendees = len(df2)

#avg age
avg_age = round(df2["Age"].mean(),2)

#Calculate the number of bootcamp attendees who self-identify as male; female; or neither.
male_attendees = round(((len(df2[df2.Gender == 'male'])/total_attendees)*100),2)
male_attendees = str(male_attendees)+"%"

female_attendees = round(((len(df2[df2.Gender == 'female'])/total_attendees)*100),2)
female_attendees = str(female_attendees)+"%"

othergender_attendees = round(((len(df2[(df2.Gender != 'male') & (df2.Gender != 'female')])/total_attendees)*100),2)
othergender_attendees = str(othergender_attendees)+"%"

#Calculate the number of bootcamp attendees who hold college degrees.

df2['SchoolDegree'].unique()
degrees = ["bachelor's degree", "master's degree (non-professional)",
       "professional degree (MBA, MD, JD, etc.)", "associate's degree",
       "Ph.D."]

#Create new column is true if college degree
df2['CollegeDegree'] = df2['SchoolDegree'].isin(degrees)

Has_Degree = df2.CollegeDegree.sum()

#Calculate the percentage of respondents who attended a bootcamp.
percent_attended = (len(df2) / len(df))
percent_attended = round((percent_attended * 100),0)
percent_attended = str(percent_attended)+"%"


#Calculate the percentage of people who attended a bootcamp and hold a college degree.
attended_plus_degree = round(((Has_Degree/len(df))*100),0)
attended_plus_degree = str(attended_plus_degree)+"%"

#Calculate the average post-bootcamp salary.
#take rows with a value for 'ExpectedEarning'
df3 = df2[np.isfinite(df2['ExpectedEarning'])]

avg_salary = round(df2["ExpectedEarning"].mean(),2)

#Create a new, two-row table collecting the above data.
final = pd.DataFrame({
    "Stats": ["Total Respondents", "Total Attendees", "Average Age of Attendee", "Male Attendees", "Female Attendees","Neither Male or Female Attendees","Attendees with College Degrees","Percent Attended","Percent Attended & Hold College Degree","Average Post-Bootcamp Salary"],
    "Values": [total_respondents, total_attendees, avg_age, male_attendees, female_attendees,othergender_attendees,Has_Degree,percent_attended,attended_plus_degree,avg_salary]
})

final = final.transpose()

#export final
final.to_csv("final.csv",header=True,index=False)
